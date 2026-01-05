import pygame as pg
import ast
import sys
import shutil
import os
import io
import base64
import zipfile
import ctypes
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

pg.init()
pg.font.init()

tk_root = tk.Tk()
tk_root.withdraw()
tk_root.update_idletasks()

encoded_base64_imgs = {
    "icon_150x150": "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",
    "icon_128x128": "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",
    "icon_64x64":   "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAFBhaW50Lk5FVCA1LjEuNBLfpoMAAAC2ZVhJZklJKgAIAAAABQAaAQUAAQAAAEoAAAAbAQUAAQAAAFIAAAAoAQMAAQAAAAMAAAAxAQIAEAAAAFoAAABphwQAAQAAAGoAAAAAAAAAo5MAAOgDAACjkwAA6AMAAFBhaW50Lk5FVCA1LjEuNAADAACQBwAEAAAAMDIzMAGgAwABAAAAAQAAAAWgBAABAAAAlAAAAAAAAAACAAEAAgAEAAAAUjk4AAIABwAEAAAAMDEwMAAAAADGeaJxF/RJFQAAA5tJREFUeF7tms9PE0EUx7cItdUSabEkRIyJHiQhHsDUHxiNJw0XT8Q/QEESiRp/HiDgXeXoTYiBg/Fk4sXEo4kXPRhPXhSCUZQKtkIrtLvt+r7tzLq7UFq8sOO+T/LNm5luD983b6aEtxrDMAzDMAzjUwIibpZ//d5WYYq4hs0awfNSwOuJkMYR7WOLWg3UkfBsPSko4jYS1r1MUahAypMMMbYSUksC8AzMNpC2kxpJITHHuperAGZhGuaXSatirJNqSgA+h2B8B6kxFmvbc2lg8kEksvtIIBDwegVohpFbmJ1992hivP8xTX+RsqTfJFSGWSkB0jiEcm8ixW7eejFGCeihsZIMDx3qovCDtEhCJRTXS4DduDzz8XB419HLg0+maOxxAlpDQ0iLRJo1qlCxVsYw8um7o4eP0XCOtEIquEsYc5xtlHszqZW0l7Svr3/8IUUFMDVdX9FSqS9aNpsSa2Xq64OoZNxh1v1lTxHG8qLbSWq5fuNpb0fH6YFgMNwSDHr7uBfNIple1KY/fRArZaLRNkcl0DHopvCRhEsxb3clyx673zQ5tfS+s7NnBObxodepo/u4ORbXEolTNPtrOJNZECMLeLYekAnAAsYwHx2fSL7CoqokEidp18vWdB2/fA7sm+6YIAk4AmG6ROKlFYXZf6BdjDbGXgEQjgDuAOWJNuEOr467AnAzIgnK4/4JrITjPBCyEnyDOwG+gxMgom/hBIjoWzgBIvoWToCIvoUTIKJv4QSI6Fs4ASL6CUdvkCtAxKqYzsSpDPqCpbYYJrUnAF/5P0BLTHaIa0+AYahfAYWCnqaAxig6xqUqcCcALis6zefVKwP0CUE6PfdydKTrOA3RLys1RrG+XgI2dIkkFIvqVEMo1Jiann47dv/e2Ss0tVdAabPlf4AR0RRBG6x1cmrpDRZVJpfL/uzvaz1HwyUS3glAREcYuy8T4KgA7Dz6SMu6vrqmoaYaw0PdvRQ+k76S5kl4OQL+LPPAnYAcKXPxQsuZ0oqiJOdnnieTM99omCGh5OELNz88Os6vvQmCMbpCuDXQHo/fvvPsfHv7iQEVeoWmaRbT6e+vr109OEhTlLssfeu8k9bg7gKhIpAE3AfyZSi8IYK5+8L0EthZ7DD+yIFpnHXsOs57RfPAnQDMIZi1vw7n9bfBYNCeBOz6uiXvppIpmQgpSaXntxppUu62VFWqGfKq4Y2oyTjDMAzDMAzjbzTtD0UG8j4Uc7gzAAAAAElFTkSuQmCC",
    "icon_32x32":   "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAFBhaW50Lk5FVCA1LjEuNBLfpoMAAAC2ZVhJZklJKgAIAAAABQAaAQUAAQAAAEoAAAAbAQUAAQAAAFIAAAAoAQMAAQAAAAMAAAAxAQIAEAAAAFoAAABphwQAAQAAAGoAAAAAAAAAo5MAAOgDAACjkwAA6AMAAFBhaW50Lk5FVCA1LjEuNAADAACQBwAEAAAAMDIzMAGgAwABAAAAAQAAAAWgBAABAAAAlAAAAAAAAAACAAEAAgAEAAAAUjk4AAIABwAEAAAAMDEwMAAAAADGeaJxF/RJFQAAAitJREFUWEdjGAWjYKABI5TGB4hRQyz4D6XhAMNwd49Sxp07ulnExTVFLa0ihf7/+0cVB/wHQkZGJoanT69+OnN61Qs1Nafft27tw2o4a0rqQndpac12ZmZWaSAfw9XkAEZGRhBm/Pv376cPH5519vf5LJCQ1P+B7ABmIOYAYtn8gg0rODh49f///weWoBT8/w/xAycnLwPQXIY/f36/OXtmg8PGjY1XYQ5g8vMrV3D3yKjn4OC2YWL6Lw8UAzmIKuDfv38Mr149A+LnDAICkgwsLKy/79497TZvbvIBmANYJ0++3ckvIFEIDCkGVlYmYHBBZagAQMEPDHqGa9fOAXlswFDg+XX79gmPBfNTDzBBlDCwAwV1QAxQcFEbg0KAmZkZGAVcYMuQAcwBTMBYokpiwwWA7sAKYA4YMDDqgFEHjFwHwItgKE1vwMTIxASqaP6jOABW/IJKL9oBULH858Xjx1eegXgwB/wH1ZZQNlABqPgEFaOQEow6GEgwMLz+9evbyVev7hXu3tX/yMIiDl7lsE2ddn8KH59IKi18D6qMQPXB9etH4jvavTcDhT7b2af/PXRw5n94lSstpXVfVExejZmZRQDoiO9A/A1KU4J/gOh///58+vTp9czqKsu5QKs+APG/hw/Pgu0Fh0B29iLGqVPjQI7hj0+YKA50MTNQI0iKYsDExMwAtPzH2jWNoDj/AcR/wRJQAI93NIBLnBxA/TgdBaOAeoCBAQCr+GnbFL3q4gAAAABJRU5ErkJggg=="
}

def calc_screen_width(prop_percent):
    global prop_width, screen_width, screen_height
    screen_width, screen_height = actual_width, actual_height
    prop_width = screen_width * prop_percent * 0.01
    screen_width *= 1 - prop_percent * 0.01

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("victormartin.pypresenter.editor")
setmode = (0,0)
screen = pg.display.set_mode(setmode)
actual_width, actual_height = pg.display.get_window_size()
calc_screen_width(1)
icon_32x32 = pg.image.load(io.BytesIO(base64.b64decode(encoded_base64_imgs['icon_32x32'])))
pg.display.set_icon(icon_32x32)
pg.display.set_caption('PyPresenter')
pres_size = 1920, 1080
canvas = pg.Surface(pres_size, pg.SRCALPHA)
clock = pg.time.Clock()


"""
slides
    background color: 0
        z_order (always -1)
        RGB color
    images: 1
        z_order
        img_id
        position
        rotation
        size
    texts: 2
        z_order
        text
        position
        rotation
        size
        RGBA
        font
"""



slides = [[[0, -1, (255, 255, 255)]]]

def get_max_z(slide):
    return max((part[1] for part in slide if part[0] != 0), default=0)

def export_slides(name):
    with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('slides.txt', repr(slides))
        
        added_images = set()
        for slide in slides:
            for part in slide:
                if part[0] == 1:
                    img_name = part[2]
                    if not img_name:
                        continue
                    if img_name not in added_images:
                        source = img_source[img_name]

                        if isinstance(source, (io.BytesIO, io.BufferedIOBase)):
                            source.seek(0)
                            data = source.read()
                        else:
                            with open(source, 'rb') as f:
                                data = f.read()

                        zf.writestr(f'images/{img_name}', data)
                        added_images.add(img_name)

def load_slides(name):
    if not name:
        return
    global slide_change
    global slides
    global img_cache
    slide_change = True
    with zipfile.ZipFile(name, 'r') as zf:
        slides_data = zf.read('slides.txt').decode('utf-8')
        slides = ast.literal_eval(slides_data)
        
        img_cache.clear()
        img_source.clear()
        
        for file_name in zf.namelist():
            if file_name.startswith('images/'):
                img_name_ext = file_name.split('/')[-1]
                
                with zf.open(file_name) as f:
                    img_bytes = f.read()
                    img_cache[img_name_ext] = pg.image.load(io.BytesIO(img_bytes)).convert_alpha()
                    img_source[img_name_ext] = io.BytesIO(img_bytes)
        
def pick_slide():
    tk_root.update()
    return filedialog.askopenfilename(
        parent=tk_root,
        title="Select Presentation",
        filetypes=[
            ("PyPresenter", "*.pypres"),
            ("All files", "*.*")
        ]
    )

    

def save_presentation():
    tk_root.withdraw()

    path = filedialog.asksaveasfilename(
        title="Save Presentation",
        defaultextension=".pypres",
        filetypes=[("PyPresenter", "*.pypres"), ("All files", "*.*")]
    )
    if path:
        export_slides(path)


if len(sys.argv) > 1:
    if "\\" not in sys.argv[1]:
        load_slides('presentations/' + sys.argv[1])
    else:
        load_slides(sys.argv[1])
    

img_cache = {}
img_source = {}
render_cache = {}
font_cache = {}
text_cache = {}

def get_img(img_id):
    if img_id not in img_cache:
        img_cache[img_id] = pg.image.load(img_source[img_id]).convert_alpha()
    return img_cache[img_id]

def get_transformed_img(name, rotation, scale):
    key = (name, rotation, tuple(scale))
    if key not in render_cache:
        img = get_img(name)
        img = pg.transform.rotate(img, rotation)
        img = pg.transform.scale_by(img,scale)
        render_cache[key] = img
    return render_cache[key]

def get_font(font_type, size):
    key = (font_type, size)
    if key not in font_cache:
        font_cache[key] = pg.font.SysFont(font_type, size)
    return font_cache[key]

def get_text(text, color, font_type, size): 
    key = (text, color, font_type, size)
    if key not in text_cache:
        text_cache[key] = get_font(font_type, size).render(text, True, color).convert_alpha()
    return text_cache[key]


def copy_image(source_path):
    if not source_path:
        return None
    os.makedirs('images', exist_ok=True)
    
    name = os.path.basename(source_path)
    destination_path = os.path.join('images', name)
    
    base, ext = os.path.splitext(name)
    i = 1
    while os.path.exists(destination_path):
        destination_path = os.path.join('images', f'{base}_{i}{ext}')
        i += 1
    
    shutil.copy2(source_path, destination_path)
    return os.path.basename(destination_path)

def pick_image():
    return filedialog.askopenfilename(
        parent=tk_root,
        title='Select image',
        filetypes=[
            ('Image files', "*.png *.jpg *.jpeg *.bmp *.gif"),
            ('All files', "*.*")
        ]
    )

def confirm(text):
    result = messagebox.askyesno(
        title="Confirm",
        message=text,
        parent=tk_root
    )
    return result

def edit_property(title, value):
    result = None

    dialog = tk.Toplevel()
    dialog.title(title)
    dialog.resizable(False, False)
    dialog.attributes("-topmost", True)

    def submit():
        nonlocal result
        result = entry.get()
        dialog.destroy()

    tk.Label(dialog, text=title).pack(padx=10, pady=(10, 5))

    entry = tk.Entry(dialog, width=30)
    entry.insert(0, str(value))
    entry.pack(padx=10, pady=5)
    entry.focus_set()

    dialog.bind("<Return>", lambda e: submit())
    dialog.bind("<Escape>", lambda e: dialog.destroy())

    tk.Button(dialog, text="OK", command=submit).pack(pady=(5, 10))

    dialog.update_idletasks()
    dialog.lift()
    dialog.grab_set()
    dialog.wait_window()

    return result




def edit_int(title, value):
    result = edit_property(title, value)
    if result is None:
        return None
    try:
        return int(result)
    except ValueError:
        return None

def edit_float(title, value):
    result = edit_property(title, value)
    if result is None:
        return None
    try:
        return float(result)
    except ValueError:
        return None

def edit_text(title, value):
    return edit_property(title, value)

def draw_elements():
    screen.fill((0,0,0))
    for part in slide:
        match part[0]:
            case 0:
                canvas.fill(part[2])
            case 1:
                rect = get_transformed_img(part[2], part[4], part[5]).get_rect(center=part[3])
                canvas.blit(get_transformed_img(part[2], part[4], part[5]), rect)
            case 2:
                canvas.blit(get_text(part[2], part[6], part[7], part[5]), part[3])
    
    if selected_part is not None:
        part = selected_part
        if part[0] == 1:
            rect = get_transformed_img(part[2], part[4], part[5]).get_rect(center=part[3])
        else:
            rect = get_text(part[2], part[6], part[7], part[5]).get_rect(topleft = part[3])
        pg.draw.rect(canvas, (80,160,255), rect, 1)
        pg.draw.rect(canvas, (80,160,255), rect.inflate(6,6), 1)
        for x, y in (
            rect.topleft, rect.topright,
            rect.bottomleft, rect.bottomright
            ):
            pg.draw.rect(canvas, (80,160,255), (x-4, y-4, 8, 8))
    
    scaled = pg.transform.smoothscale(canvas, scaled_size)
    screen.blit(scaled, (lbox_x_offset, lbox_y_offset))


def create_button(text, font, i, x_pos, y_pos, pressable):
    global top_buttons_collision
    renderable_text = get_text(text, (255,255,255), font, int(12 * gui_scale))
    text_bounds = renderable_text.get_rect()
    text_bounds.midleft = (x_pos, y_pos)
    text_bounds = text_bounds.inflate(int(16 * gui_scale), int(7 * gui_scale))
    if text_bounds.collidepoint(m_pos) and pressable:
        if mouse_clicked:
            top_buttons_collision[i] = True
        pg.draw.rect(screen, (68, 68, 68), text_bounds)
    else:
        if pressable:
            pg.draw.rect(screen, (58,58,58), text_bounds)
        else:
            pg.draw.rect(screen, (48,48,48), text_bounds)
    screen.blit(renderable_text, (x_pos, y_pos - 6 * gui_scale))
    return text_bounds

buttons = ('New', 'Open', 'Save', 'Add Text', 'Add Image', 'Present', 'Delete Slide')

def draw_gui():
    global top_buttons_collision
    if not presenting:
        pg.draw.rect(screen, (43,43,43), (0,0,actual_width,actual_height*0.045))
        pg.draw.line(screen, (68,68,68), (0,actual_height*0.045), (actual_width, actual_height*0.045))
        x_pos = 20*gui_scale
        i = 0
        for text in buttons:
            pressable = True
            if text == 'Delete Slide' and slide_idx == 1:
                pressable = False
            text_bounds = create_button(text, 'dejavusans', i, x_pos, actual_height*0.0225, pressable)
            x_pos += text_bounds.w + 15 * gui_scale
            i += 1
        y_pos = actual_height*0.0225
    else:
        y_pos = actual_height*(1-0.0225)
        pg.draw.rect(screen, (43,43,43), (actual_width*0.4625,actual_height*0.96,actual_width*0.075,actual_height*0.035))
    text = get_text(f'{slide_idx} / {len(slides)}', (255,255,255), 'CASCADIAMONO', int(18*gui_scale))
    text_width = text.get_rect().width
    screen.blit(text, ((actual_width - text_width)*0.5, y_pos - 6 * gui_scale))

    create_button('<', 'sitkatext', len(buttons), int(actual_width * 0.5 - 50 * gui_scale), y_pos, slide_idx != 1)
    text = '>'
    if slide_idx >= len(slides) and not presenting:
        text = '+'
    create_button(text, 'sitkatext', len(buttons) + 1, actual_width * 0.5 + 41 * gui_scale, y_pos, True)

# 0: Single Values
# 1: Two Values
# 2: Color Picker
# 3: Text

def get_properties(part):
    if part[0] == 1:  
        return [
            ("Position",    part[3], 0,  64, 1),
            ("Rotation",    part[4], 4,  64, 0),
            ("Scale",       part[5], 0,  64, 1),
        ]

    if part[0] == 2: 
        return [
            ("Position",    part[3], 0,  64, 1),
            ("Text",        part[2], 2,  64, 3),
            ("Font",        part[7], 2,  64, 3),
            ("Font Size",   part[5], 5,  64, 0),
            ("Color",       part[6], 5,  64, 2)
        ]

    return []

prop_screen_percent = 9
def draw_properties():
    global prop_anim, prop_view, selected_part, slide_change
    calc_screen_width(prop_anim)
    arrow = get_text('|', (255,255,255,255), 'sitkatext', int(24*gui_scale))
    if not prop_view and prop_anim == 1:
        arrow = get_text('<', (255,255,255,255), 'sitkatext', int(24*gui_scale))
        if pg.Rect(screen_width, 0, prop_width, screen_height).collidepoint(m_pos) and mouse_clicked:
            prop_anim += 0.5
    if not prop_view and prop_anim != 1:
        if prop_anim < prop_screen_percent: prop_anim += 0.5
        else: prop_view = True
    if prop_view and prop_anim == prop_screen_percent:
        arrow = get_text('>', (255,255,255,255), 'sitkatext', int(24*gui_scale))
        if arrow.get_rect(topleft=(screen_width, screen_height*0.5)).inflate(20, 20).collidepoint(m_pos) and mouse_clicked:
            prop_anim -= 0.5
    if prop_view and prop_anim != prop_screen_percent:
        if prop_anim != 1: prop_anim -= 0.5
        else: prop_view = False
    
    pg.draw.rect(screen, (50, 50, 50), (screen_width, 0, prop_width, screen_height))
    screen.blit(arrow, (screen_width, screen_height*0.5))
    
    if selected_part and prop_view and prop_anim == prop_screen_percent:
        properties = get_properties(selected_part)
        y = actual_height * 0.2
        for prop in properties:
            text = get_text(prop[0], (255,255,255,255), 'dejavusans', int(18*gui_scale))
            screen.blit(text, (screen_width*1.013, y))
            match prop[4]:
                case 0:
                    text = get_text(str(round(prop[1], 1)), (255,255,255,255), 'dejavusans', int(14*gui_scale))
                    pos = (screen_width*1.013, y + int(22*gui_scale))
                    rect = text.get_rect(topleft=pos).inflate(10, 10)
                    screen.blit(text, pos)
                    if rect.collidepoint(m_pos) and mouse_clicked:
                        new = edit_float(prop[0], prop[1])
                        if new is not None:
                            if prop[0] == "Rotation":
                                selected_part[4] = new
                            elif prop[0] == "Font Size":
                                selected_part[5] = int(new)

                            slide_change = True
                case 1:
                    value = prop[1]

                    label = f"{value[0]:.1f}, {value[1]:.1f}"
                    text = get_text(label, (255,255,255,255),
                                    'dejavusans', int(14*gui_scale))
                    pos = (screen_width*1.013, y + int(22*gui_scale))
                    rect = text.get_rect(topleft=pos).inflate(10, 10)

                    screen.blit(text, pos)

                    if rect.collidepoint(m_pos) and mouse_clicked:
                        x = edit_float(prop[0] + " X", value[0])
                        yv = edit_float(prop[0] + " Y", value[1])
                        if x is not None and yv is not None:
                            value[0] = x
                            value[1] = yv
                            slide_change = True
                            
                case 2:
                    value = prop[1]
                    label = f"{value[0]}, {value[1]}, {value[2]}, {value[3]}"
                    text = get_text(label, (255,255,255,255), 'dejavusans', int(14*gui_scale))
                    pos = (screen_width*1.013, y + int(22*gui_scale))
                    rect = text.get_rect(topleft=pos).inflate(10, 10)

                    color_box = (screen_width*1.017 - int(28*gui_scale), y + int(22*gui_scale))
                    pg.draw.rect(screen, tuple(value[:3]), (color_box[0], color_box[1], int(18*gui_scale), int(14*gui_scale)))

                    screen.blit(text, pos)

                    if rect.collidepoint(m_pos) and mouse_clicked:
                        picked = colorchooser.askcolor(color=(value[0], value[1], value[2]), parent=tk_root)
                        if picked and picked[0] is not None:
                            r, g, b = picked[0]
                            a = value[3] if len(value) > 3 else 255
                            selected_part[6] = (int(r), int(g), int(b), int(a))
                            slide_change = True

                case 3:
                    text_val = prop[1]
                    preview = (text_val[:20] + ("…" if len(text_val) > 20 else "")) if isinstance(text_val, str) else str(text_val)

                    text = get_text(preview, (255,255,255,255), 'dejavusans', int(14*gui_scale))
                    pos = (screen_width*1.013, y + int(22*gui_scale))
                    rect = text.get_rect(topleft=pos).inflate(10, 10)

                    screen.blit(text, pos)

                    if rect.collidepoint(m_pos) and mouse_clicked:
                        title = "Edit Text" if prop[0] == "Text" else "Edit Font" if prop[0] == "Font" else prop[0]
                        new = edit_text(title, text_val)
                        if new is not None:
                            if prop[0] == "Text":
                                selected_part[2] = new
                            elif prop[0] == "Font":
                                selected_part[7] = new

                            slide_change = True
                
            y += gui_scale * prop[3]
    
    
    

def new_img_id(source_path):
    base_id = f"img_{len(img_source)}"
    ext = os.path.splitext(source_path)[1]
    return base_id + ext


def add_new_image():
    global slide_change
    global slides

    image_pick = pick_image()
    if image_pick:
        image_id = new_img_id(image_pick)
        img_source[image_id] = image_pick
        img_cache[image_id] = pg.image.load(image_pick).convert_alpha()
        slides[slide_idx - 1].append([1, get_max_z(slide) + 1, image_id, [screen_width*0.5, screen_height*0.5], 0, [0.5, 0.5]])
        slide_change = True

        #0 type
        #1 z_order
        #2 text
        #3 position
        #4 rotation
        #5 size
        #6 RGBA
        #7 font

def add_new_text():
    slides[slide_idx - 1].append([2, get_max_z(slide) + 1, "Edit Text", [pres_size[0] * 0.5, pres_size[1] * 0.5], 0, 48, (0,0,0,255), "dejavusans"])

def check_collisions():
    global slide_change, dragging, selected_part, drag_offset
    if selected_part is not None and not presenting:
        return
    for part in reversed(slide):
        if part[0] != 0:
            if part[0] == 1:
                img = get_transformed_img(part[2], part[4], part[5])
                rect = img.get_rect(center=part[3])
            else:
                surf = get_text(part[2], part[6], part[7], part[5])
                rect = surf.get_rect(topleft = part[3])
                
            if rect.collidepoint(m_pos_pres):
                selected_part = part
                selected_part[1] = get_max_z(slide) + 1
                drag_offset = (
                    selected_part[3][0] - m_pos_pres[0],
                    selected_part[3][1] - m_pos_pres[1]
                )
                slide_change = True
                dragging = True
                break
            
def consume_key(key):
    if key in key_once:
        key_once.remove(key)
        return True
    return False


MOVE_KEYS = (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN)
KEY_REPEAT_DELAY = 300
KEY_REPEAT_RATE  = 16
key_hold_time = {}
key_once = set()


prop_anim = 1
prop_view = False
prev_scale = None
scale = 1
dragging = False
selected_part = None
drag_offset = (0, 0)
slide_change = True
slide_idx = 1
presenting = False
running = True
while running:
    clock.tick(60)
    
    if scale != prev_scale:
        render_cache.clear()
        prev_scale = scale
    
    mouse_clicked = False
    top_buttons_collision = [False, False, False, False, False, False, False, False, False]
    
    scale = min(screen_width / pres_size[0], screen_height / pres_size[1])
    gui_scale = min(actual_width / pres_size[0], actual_height / pres_size[1])
    scaled_size = (int(pres_size[0] * scale), int(pres_size[1] * scale))
    lbox_x_offset = int((screen_width - scaled_size[0]) * 0.5)
    lbox_y_offset = int((screen_height - scaled_size[1]) * 0.5)
    
    m_pos = pg.mouse.get_pos()
    m_pos_pres = (m_pos[0] - lbox_x_offset) / scale, (m_pos[1] - lbox_y_offset) / scale
    m_pos_pres = (max(0, min(pres_size[0], m_pos_pres[0])), max(0, min(pres_size[1], m_pos_pres[1])))
    
    in_editor = True
    if m_pos_pres[0] <= 0 or m_pos_pres[1] <= 0 or m_pos_pres[0] > screen_width or m_pos_pres[1] > screen_height or presenting:
        in_editor = False
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            key_once.add(event.key)
            if event.key in MOVE_KEYS:
                key_hold_time[event.key] = pg.time.get_ticks()
            if event.key == pg.K_i and event.mod & pg.KMOD_CTRL and not presenting:
                top_buttons_collision[4] = True
            if event.key == pg.K_t and event.mod & pg.KMOD_CTRL and not presenting:
                top_buttons_collision[3] = True
            if event.key == pg.K_ESCAPE:
                presenting = False
        elif event.type == pg.KEYUP:
            key_once.discard(event.key)
            key_hold_time.pop(event.key, None)
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_clicked = True
            if in_editor:
                selected_part = None
                check_collisions()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            dragging = False

    if selected_part:
        if consume_key(pg.K_DELETE):
            slide.remove(selected_part)
            selected_part = None
            slide_change = True
    else:
        if consume_key(pg.K_LEFT) and slide_idx > 1:
            top_buttons_collision[7] = True

        if consume_key(pg.K_RIGHT):
            top_buttons_collision[8] = True
    
    pressed = pg.key.get_pressed()
    if selected_part:
        for key in MOVE_KEYS:
            if key in key_hold_time:
                held_for = pg.time.get_ticks() - key_hold_time[key]
                moved = False
                if consume_key(key):
                    moved = True
                elif held_for >= KEY_REPEAT_DELAY:
                    if (held_for - KEY_REPEAT_DELAY) // KEY_REPEAT_RATE != ((held_for - KEY_REPEAT_DELAY - clock.get_time()) // KEY_REPEAT_RATE):
                        moved = True
                x, y = selected_part[3]
                if moved:
                    if key == pg.K_LEFT: x -= 1
                    if key == pg.K_RIGHT: x += 1
                    if key == pg.K_UP: y -= 1
                    if key == pg.K_DOWN: y += 1
                    selected_part[3] = (x, y)
    
    if dragging and not presenting:
        selected_part[3] = [
            m_pos_pres[0] + drag_offset[0],
            m_pos_pres[1] + drag_offset[1]
        ]
    
    if slide_change and not dragging or (slide_change and pg.MOUSEBUTTONDOWN and dragging):
        if len(slides) <= slide_idx - 1:
            if presenting:
                slide_idx -= 1
                presenting = False
            else:
                slides.append([[0, -1, (255, 255, 255)]])
        slide = slides[slide_idx - 1]
        slide.sort(key=lambda e: e[1])
        slide_change = False
    
    draw_elements()
    if not presenting:
        draw_properties()
    draw_gui()
    
    if not dragging:
        if top_buttons_collision[0]:
            if confirm("Are you sure you want to create a new presentation?"):
                slides = [[[0, -1, (255, 255, 255)]]]
                slide_change = True
                slide_idx = 1
        if top_buttons_collision[1]:
            path = pick_slide()
            if path:
                if confirm("Are you sure you want to load this presentation?"):
                    load_slides(path)
        if top_buttons_collision[2]:
            save_presentation()
        if top_buttons_collision[3]:
            add_new_text()
        if top_buttons_collision[4]:
            add_new_image()
        if top_buttons_collision[5]:
            presenting = True
            calc_screen_width(0)
        if top_buttons_collision[6]:
            if confirm("Are you sure you want to delete this slide?"):
                slides.remove(slide)
                slide_idx = min(slide_idx - 1, slide_idx)
                selected_part = None
                slide_change = True
        if top_buttons_collision[7]:
            slide_idx -= 1
            selected_part = None
            slide_change = True
        if top_buttons_collision[8]:
            slide_idx += 1
            selected_part = None
            slide_change = True
    
    
    pg.display.flip()