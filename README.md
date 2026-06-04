# FogTrack: Vision-Language Inheritance Learning for Aerial Multi-Vessel Tracking

**Changhong Fu\*, Zijie Zhang, Mengyuan Li, Liangliang Yao, Haobo Zuo, Guangze Zheng, Shan An**

\* Corresponding author.

## Abstract
Real-time UAV multi-vessel tracking plays a pivotal role in maritime safety and surveillance, but is critically impeded by dynamic maritime fog. Under such adverse conditions, conventional tracking pipelines suffer from severe feature collapse and temporal flickering. Furthermore, existing enhancement methods entail prohibitive latency unsuitable for edge deployment, while standard domain adaptation relies on vulnerable visual cues, overlooking robust semantic knowledge. To reconcile state-of-the-art accuracy with strict edge constraints, we propose a language-guided progressive inheritance learning framework, termed FogTrack. We first construct a physics-aware fog synthetic engine to generate homologous stochastic fog streams. Next, to realize this progressive inheritance, a three-stage feature-language isomorphic distillation is designed to progressively restore the representations of the visual student network. Since high-level semantics are significantly more resilient to fog degradation than low-level pixel features, we leverage robust vision-language (VL) representations as offline semantic anchors to perform text-aligned semantic grounding, semantic-driven clarity alignment, and enforce trajectory continuity via a novel instance-level temporal consistency loss. Crucially, this inheritance paradigm successfully transfers degradation-invariant knowledge from heavy foundation models to resource-constrained edge devices. By internalizing this VL knowledge into the visual latent space during training, FogTrack deploys a fully decoupled, purely vision-based lightweight pipeline without multimodal computational overhead. Extensive experiments demonstrate that FogTrack achieves state-of-the-art tracking performance and robustness against dynamic maritime fog, while ensuring real-time UAV edge inference.

## Repository Layout

| Path | Description |
| --- | --- |
| `ultralytics/` | Detector code and training scripts |
| `ultralytics/train_foggy.py` | Phase 1/2 training |
| `ultralytics/train_foggy_p3.py` | Phase 3 training |
| `ultralytics/cfg/models/` | Model definitions |
| `ultralytics/weights/` | Detector weights |
| `tracker/` | Tracker code |
| `tracker/track.py` | Tracking implementation |
| `tracker/trackers/` | Tracker implementations |
| `eval/` | TrackEval wrapper |
| `CLIP-main/` | CLIP source |
| `weights/` | Text anchors and ReID weights |
| `track-results/` | Example tracking results |
| `eval_vesselmot_test.py` | Example evaluation script |

## Environment

```bash
conda create -n fogtrack python=3.11 -y
conda activate fogtrack
pip install -r requirement.txt
```

## Dataset Preparation

### FogMVT Dataset

**Download (Baidu Netdisk):** https://pan.baidu.com/s/1ExifXrPfVasiR6ByTepl8Q?pwd=k3r9

### Training / Evaluation Data

The default FogMVT tracking config is `tracker/config_files/fogmot.yaml`.

```text
datasets/fogmot/
+-- test/
    +-- <sequence_name>/
        +-- img1/
        |   +-- 000001.jpg
        |   +-- ...
        +-- gt/
            +-- gt.txt
+-- train/
    +-- ...
+-- val/
    +-- ...
```

## Training

Phase 1/2 detector training:

```bash
python ultralytics/train_foggy.py
```

Phase 3 temporal training:

```bash
python ultralytics/train_foggy_p3.py
```

## Tracking

Run FogTrack on the FogMVT test split:

```bash
python tracker/track.py --dataset fogmot --detector Tconv --tracker bytetrack --kalman_format byte
```

## Evaluation

```bash
python eval_vesselmot_test.py
```

The example result summary in `track-results/vessel_summary.txt` reports:

```text
HOTA 44.744
DetA 36.059
AssA 57.765
MOTA 35.266
IDF1 47.670
```
## Citation

If you find this work useful in your research, please cite:
```text
@inproceedings{fogtrack2026cisram,
  author    = {Changhong Fu and Zijie Zhang and Mengyuan Li and Liangliang Yao and Haobo Zuo and Guangze Zheng and Shan An},
  title     = {FogTrack: Vision-Language Inheritance Learning for Aerial Multi-Vessel Tracking},
  booktitle = {IEEE International Conference on Cybernetics and Intelligent Systems (CIS) and IEEE Conference on Robotics, Automation and Mechatronics (RAM)},
  year      = {2026},
  publisher = {IEEE}
}
```

## Acknowledgements

This project builds on:

- https://github.com/openai/CLIP
- https://github.com/YanZhang-zy/BiLaLoRA
- https://github.com/JonathonLuiten/TrackEval
- https://github.com/ultralytics/ultralytics
- https://github.com/JackWoo0831/Yolov7-tracker

We thank the original authors for their contributions.

## Contact

If you have any questions, please contact me.

Zijie Zhang

Email: [2410022@tongji.edu.cn](mailto:2410022@tongji.edu.cn)
