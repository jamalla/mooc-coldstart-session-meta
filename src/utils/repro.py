from __future__ import annotations

import os
import random
from dataclasses import dataclass

import numpy as np

try:
    import torch
except Exception:
    torch = None


@dataclass(frozen=True)
class ReproConfig:
    seed: int = 42
    deterministic: bool = True


def set_seed(cfg: ReproConfig) -> None:
    os.environ["PYTHONHASHSEED"] = str(cfg.seed)

    random.seed(cfg.seed)
    np.random.seed(cfg.seed)

    if torch is not None:
        torch.manual_seed(cfg.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(cfg.seed)

        if cfg.deterministic:
            # Safe defaults for reproducibility
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
            try:
                torch.use_deterministic_algorithms(True)
            except Exception:
                pass
