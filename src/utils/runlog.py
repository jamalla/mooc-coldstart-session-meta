from __future__ import annotations

import json
import os
import platform
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

try:
    import torch
except Exception:
    torch = None


@dataclass(frozen=True)
class RunInfo:
    run_id: str
    created_utc: str
    python: str
    platform: str
    torch: str | None
    cuda_available: bool | None
    cuda_version: str | None
    device_count: int | None


def make_run_id(prefix: str = "run") -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{ts}"


def collect_run_info(run_id: str) -> RunInfo:
    torch_ver = None if torch is None else getattr(torch, "__version__", None)
    cuda_ok = None if torch is None else bool(torch.cuda.is_available())
    cuda_ver = None if torch is None else getattr(torch.version, "cuda", None)
    dev_cnt = None if torch is None else int(torch.cuda.device_count())

    return RunInfo(
        run_id=run_id,
        created_utc=datetime.now(timezone.utc).isoformat(),
        python=platform.python_version(),
        platform=f"{platform.system()} {platform.release()}",
        torch=torch_ver,
        cuda_available=cuda_ok,
        cuda_version=cuda_ver,
        device_count=dev_cnt,
    )


def ensure_dirs(*paths: str) -> None:
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)


def write_json(path: str, payload: Dict[str, Any]) -> None:
    Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def write_run_meta(runs_dir: str, info: RunInfo, extra: Dict[str, Any] | None = None) -> str:
    out = asdict(info)
    if extra:
        out["extra"] = extra
    meta_path = str(Path(runs_dir) / info.run_id / "meta.json")
    write_json(meta_path, out)
    return meta_path
