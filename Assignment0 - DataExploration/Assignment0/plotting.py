import os
import matplotlib.pyplot as plt
from metadata import Metadata


def plot_images_per_category ( meta_data, save=False ):
    plt.clf()
    plt.rcParams['figure.figsize'] = [12, 6]
    plt.rcParams['figure.dpi'] = 100
    images_per_category = {cat['id']:[] for cat in meta_data.categories}
    for im in meta_data.images:
        images_per_category[meta_data.im_to_cat[im['id']]].append(im['id'])
    ind = range(len(meta_data.categories))
    sorted_cats = sorted(meta_data.categories, key=lambda cat: len(images_per_category[cat['id']]), reverse=True)
    plt.bar(ind,[len(images_per_category[cat['id']]) for cat in sorted_cats],edgecolor = 'b', log=True)
    plt.xlabel('Category')
    plt.ylabel('Number of images')
    plt.title('Images per category')
    plt.grid(b=None)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=True, top=False)
    plt.tick_params(axis='y', which='both', right=False, left=True)
    if save:
        os.makedirs('figs', exist_ok=True)
        plt.savefig('figs/images_per_category.png')
    else:
        plt.show()

def plot_images_per_category_per_location ( meta_data, save=False ):
    plt.clf()
    plt.rcParams['figure.figsize'] = [12, 6]

    images_per_category = {cat['id']:[] for cat in meta_data.categories}
    for im in meta_data.images:
        images_per_category[meta_data.im_to_cat[im['id']]].append(im['id'])
    ind = range(len(meta_data.categories))
    sorted_cats = sorted(meta_data.categories, key=lambda cat: len(images_per_category[cat['id']]), reverse=True)

    images_per_category_per_loc = {loc:{cat['id']:[] for cat in meta_data.categories} for loc in meta_data.locations}
    for im in meta_data.images:
        images_per_category_per_loc[im['location']][meta_data.im_to_cat[im['id']]].append(im['id'])
    ind = range(len(meta_data.categories))
    locs = [meta_data.locations[1], meta_data.locations[2], meta_data.locations[3]]
    for idx, loc in enumerate(locs):
        plt.subplot(3,1,idx+1)
        plt.bar(ind,[len(images_per_category_per_loc[loc][cat['id']]) for cat in sorted_cats], log=True)
        plt.xlabel('Category')
        plt.ylabel('Number of images')
        plt.title('Location: '+str(loc))
        plt.grid(b=None)
        plt.tight_layout()
        plt.tick_params(axis='x', which='both', bottom=True, top=False)
        plt.tick_params(axis='y', which='both', right=False, left=True)
    if save:
        os.makedirs('figs', exist_ok=True)
        plt.savefig('figs/images_per_category_per_location.png')
    else:
        plt.show()

def plot_images_per_location(meta_data, save=False):
    plt.clf()
    images_per_location = {loc:[] for loc in meta_data.locations}
    for im in meta_data.images:
        images_per_location[im['location']].append(im['id'])
    ind = range(len(meta_data.locations))
    plt.bar(ind,sorted([len(images_per_location[loc]) for loc in meta_data.locations],reverse=True),edgecolor = 'b', log=True)
    plt.xlabel('Location')
    plt.ylabel('Number of images')
    plt.title('Images per location')
    plt.grid(b=None)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=True, top=False)
    plt.tick_params(axis='y', which='both', right=False, left=True)
    if save:
        os.makedirs('figs', exist_ok=True)
        plt.savefig('figs/images_per_location.png')
    else:
        plt.show()

def plot_categories_per_location(meta_data, save=False):
    plt.clf()
    categories_per_location = {loc:[] for loc in meta_data.locations}
    for im in meta_data.images:
        categories_per_location[im['location']].append(meta_data.im_to_cat[im['id']])
    ind = range(len(meta_data.locations))
    plt.bar(ind,sorted([len(list(set(categories_per_location[loc]))) for loc in meta_data.locations],reverse=True),edgecolor = 'b', log=True)
    plt.xlabel('Location')
    plt.ylabel('Number of images')
    plt.title('Categories per location')
    plt.grid(b=None)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=True, top=False)
    plt.tick_params(axis='y', which='both', right=False, left=True)
    if save:
        os.makedirs('figs', exist_ok=True)
        plt.savefig('figs/categories_per_location.png')
    else:
        plt.show()

def plot_images_per_sequence(metadata, save=False):
    plt.clf()
    images_per_sequence = {seq:[] for seq in metadata.sequences}
    for im in metadata.images:
        images_per_sequence[im['seq_id']].append(im['id'])
    ind = range(len(metadata.sequences))
    plt.bar(ind,sorted([len(images_per_sequence[seq]) for seq in metadata.sequences],reverse=True),edgecolor = 'b', log=True)
    plt.xlabel('Sequence')
    plt.ylabel('Number of images')
    plt.title('Images per sequence')
    plt.grid(b=None)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=True, top=False)
    plt.tick_params(axis='y', which='both', right=False, left=True)
    if save:
        os.makedirs('figs', exist_ok=True)
        plt.savefig('figs/images_per_sequence.png')
    else:
        plt.show()

def plot_boxes_per_image(detections, metadata, save=False):
    plt.clf()
    threshold = 0.6
    images_per_num_boxes = {}
    for im in detections['images']:
        im_id = im['file'].split('/')[1].replace('.jpg', '')
        if im_id in metadata.im_to_cat:
            if len(im['detections']) not in images_per_num_boxes:
                images_per_num_boxes[len(im['detections'])] = []
            images_per_num_boxes[len(im['detections'])].append(im_id)
    boxes = sorted(images_per_num_boxes.keys())
    plt.bar(boxes,[len(images_per_num_boxes[num_box]) for num_box in boxes],edgecolor = 'b', log=True)
    plt.xlabel('Number of boxes')
    plt.ylabel('Number of images')
    plt.title('Number of boxes per image')
    plt.grid(b=None)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=True, top=False)
    plt.tick_params(axis='y', which='both', right=False, left=True)
    if save:
        os.makedirs('figs', exist_ok=True)
        plt.savefig('figs/boxes_per_image.png')
    else:
        plt.show()