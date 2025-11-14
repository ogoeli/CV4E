import json

class Metadata:
    def __init__(self, filename):
        with open(filename) as f:
            metadata = json.load(f)

        # The metadata follows the COCO-CameraTraps data standard
        # https://github.com/microsoft/CameraTraps/blob/master/data_management/README.md
        
        self.images = metadata['images']
        self.annotations = metadata['annotations']
        self.train_categories = set([ann['category_id'] for ann in self.annotations])
        self.categories = [cat for cat in metadata['categories'] if cat['id'] in self.train_categories]
        self.locations = list(set(im['location'] for im in self.images))
        self.sequences = list(set(im['seq_id'] for im in self.images))
        self.im_to_cat = {ann['image_id']: ann['category_id'] for ann in self.annotations}

    def show(self):
        print('High-level statistics:\n')
        print('Images: '+str(len(self.images)))
        print('Categories: '+str(len(self.categories)))
        print('Annotations: '+str(len(self.annotations)))
        print('Animal images: '+str(len([ann['id'] for ann in self.annotations if ann['category_id'] != 0])))
        print('Empty images: '+str(len([ann['id'] for ann in self.annotations if ann['category_id'] == 0])))
        print('Locations: '+str(len(self.locations)))
        print('Sequences: '+str(len(self.sequences)))