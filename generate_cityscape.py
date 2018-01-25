import os
import time
import numpy as np
import json
import glob

ROOT_DIR = os.getcwd()

json_path_dict = {
	"train": "train/",
	"val": "val/",
	"test": "test/",
}

subset = "train"


subset_dir = os.path.join(ROOT_DIR, "gtFine", json_path_dict[subset])
# print(subset_dir)
# for root, dirs, files in os.walk(subset_dir):
# 	print('\n')
# 	print(root)
# 	print(dirs)
# 	print(files)

json_files_dir = glob.glob(subset_dir + "*/*.json")
# print(json_files_dir)

# with open("merged_subset.json", "wb") as outfile:
# 	outfile.write('[{}]'.format(','.join([open(f, "rb").read() for f in json_files_dir])))
c = 0

json_final_data = []
for json_file in json_files_dir:
	with open(json_file, 'r') as f:
		data = json.load(f)
		# _leftImg8bit.png
	image_id = os.path.basename(json_file[0:-21])
	data['image_id'] = image_id
	image_path = os.path.join(os.path.abspath('../'), 'images', json_path_dict[subset], image_id+ '_leftImg8bit.png')
	data['path'] = image_path
	for i, instance in enumerate(data['objects']):
		# segm = np.array(instance['polygon'])
		# segm = segm.reshape(1, segm.size).tolist()
		# data['objects'][i]['segmentaion'] = segm
		data['objects'][i]['segmentaion'] = data['objects'][i]['polygon']
		data['objects'][i].pop('polygon')
	# if c == 2:
	# 	print(data['objects'])
	# 	print(data['id'])\

	json_final_data.append(data)

with open(subset + '_all.json', 'w') as f:
	json.dump(json_final_data, f)
