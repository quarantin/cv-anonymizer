#!/usr/bin/env python3

import os
import sys
import zipfile

from os.path import join
from tempfile import TemporaryDirectory


def anonymize(src):

	PATTERN_1 = '<table:table '
	PATTERN_2 = '</table:table>'

	dst = src.replace('.odt', '_anon.odt')

	tmp_dir = TemporaryDirectory()
	extract_dir = tmp_dir.name

	zipdata = zipfile.ZipFile(src)
	zipdata.extractall(extract_dir)

	content = join(extract_dir, 'content.xml')

	with open(content) as fd:
		xml = fd.read()
		index1 = xml.find(PATTERN_1)
		index2 = xml.find(PATTERN_2)

		if index1 < 0 or index2 < 0:
			print("No table found, skipping document!")
			tmp_dir.cleanup()
			return

		newxml = xml[0:index1] + xml[index2 + len(PATTERN_2):]

	with open(content, 'w') as fd:
		fd.write(newxml)

	with zipfile.ZipFile(dst, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as fd:
		zipinfos = zipdata.infolist()
		for zipinfo in zipinfos:
			filename = zipinfo.filename
			filepath = join(extract_dir, filename)
			fd.write(filepath, filename)

	tmp_dir.cleanup()


if __name__ == '__main__':

	if len(sys.argv) < 2:
		print("Usage: %s <file.odt>..." % sys.argv[0])
		sys.exit()

	for src in sys.argv[1:]:
		print('Anonymzing ' + src)
		anonymize(src)
