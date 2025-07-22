from lerobot.datasets.lerobot_dataset import MultiLeRobotDataset


# repo_ids: list[str],
# root: str | Path | None = None,
# episodes: dict | None = None,
# image_transforms: Callable | None = None,
# delta_timestamps: dict[list[float]] | None = None,
# tolerances_s: dict | None = None,
# download_videos: bool = True,
# video_backend: str | None = None,

multidataset = MultiLeRobotDataset(
    repo_ids=[
        "sm1lla/pick_and_place_bb",
        "sm1lla/pick_and_place_bb1",
        "sm1lla/pick_and_place_bb2",
    ]
)
pass
