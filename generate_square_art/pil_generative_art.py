#!/bin/python
#%%
from PIL import Image, ImageDraw
import random, uuid, os
import numpy as np


def mkdir_if_dne(out_dir_path: str):
    """Make passed in directory, if it doesn't already exist.

    Args:
        out_dir_path (str): Path to desired output dir.
    """
    if not os.path.exists(out_dir_path):
        os.makedirs(out_dir_path)
    return


def get_run_id():
    """Get run id.

    Returns:
        uuid.UUID: Run uuid.
    """
    run_id = uuid.uuid1()
    print(f"Processing run_id: {run_id}")
    return run_id


def generate_and_save_square_art(
    img_out_path="./outputs/foo.png",
    canvas_size=(2000, 2000),
    rect_dims=(100, 100),
    number_of_squares=random.randint(10, 550),
):
    """Generate and save art of colored squares randomly distributed on the canvas.

    Args:
        image_size (tuple, optional): Size of overall canvas. Defaults to (2000, 2000).
        rect_dims (tuple, optional): Dimensions for rectangles width and height. Defaults to (100, 100).
        number_of_squares (int, optional): Number of squares drawn on canvas.
    """
    image = Image.new("RGB", canvas_size)
    width, height = image.size

    rectangle_width = rect_dims[0]
    rectangle_height = rect_dims[1]

    draw_image = ImageDraw.Draw(image)
    for i in range(number_of_squares):
        rectangle_x = random.randint(0, width)
        rectangle_y = random.randint(0, height)

        rectangle_shape = [
            (rectangle_x, rectangle_y),
            (rectangle_x + rectangle_width, rectangle_y + rectangle_height),
        ]
        draw_image.rectangle(
            rectangle_shape,
            fill=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        )

    image.save(img_out_path)
    return


#%%
if __name__ == "__main__":
    out_dir_path = "./outputs"
    mkdir_if_dne(out_dir_path)

    for dimval in np.arange(60, 300, 10):
        seed_val = random.randint(5, dimval)
        random.seed(seed_val)
        number_of_squares = random.randint(5, dimval)

        run_id = uuid.uuid1()
        get_run_id()

        img_out_path = f"{out_dir_path}/square_dims_{dimval}_{dimval}_number_of_squares_{number_of_squares}_seed_val_{seed_val}_runid_{run_id}.png"
        generate_and_save_square_art(
            img_out_path=img_out_path,
            canvas_size=(2000, 2000),
            rect_dims=(dimval, dimval),
            number_of_squares=number_of_squares,
        )
