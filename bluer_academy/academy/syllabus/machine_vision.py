from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "machine-vision",
    [
        "opencv",
        "pytorch",
        "[image classification](https://github.com/kamangir/bluer-algo/blob/main/bluer_algo/docs/image_classifier)",
        "[target tracking](https://github.com/kamangir/bluer-algo/blob/main/bluer_algo/docs/tracker)",
        "[yolo](https://github.com/kamangir/bluer-algo/blob/main/bluer_algo/docs/yolo)",
    ],
    duration=12,
    requires="python,bash",
)
