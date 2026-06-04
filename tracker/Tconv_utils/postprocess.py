from utils.general import scale_coords


def postprocess(out, img, ori_img):

    import torch

    out = out[0].boxes
    boxes = out.data  # [x1, y1, x2, y2, conf, cls]

    img_h, img_w = img.shape[2:]  
    ori_h, ori_w = ori_img.shape[:2]  


    scale = min(img_w / ori_w, img_h / ori_h)
    new_w = int(ori_w * scale)
    new_h = int(ori_h * scale)


    pad_x = (img_w - new_w) / 2
    pad_y = (img_h - new_h) / 2

    if len(boxes) > 0:
        resized_boxes = boxes.clone()

        resized_boxes[:, [0, 2]] = resized_boxes[:, [0, 2]] - pad_x  
        resized_boxes[:, [0, 2]] = resized_boxes[:, [0, 2]] / scale  


        resized_boxes[:, [1, 3]] = resized_boxes[:, [1, 3]] - pad_y  
        resized_boxes[:, [1, 3]] = resized_boxes[:, [1, 3]] / scale  

        resized_boxes[:, [0, 2]] = torch.clamp(resized_boxes[:, [0, 2]], 0, ori_w)
        resized_boxes[:, [1, 3]] = torch.clamp(resized_boxes[:, [1, 3]], 0, ori_h)

        return resized_boxes
    else:
        return boxes