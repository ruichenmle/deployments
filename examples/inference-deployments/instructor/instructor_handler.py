# Copyright 2022 MosaicML Examples authors
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Dict

import torch
from InstructorEmbedding import INSTRUCTOR


class HFInstructorHandler():
    """Custom Hugging Face Instructor Model handler class."""

    MODEL_NAME = ''

    def __init__(self, model_name: str):
        self.device = torch.cuda.current_device()
        self.model_name = model_name

        self.model = INSTRUCTOR(self.model_name)
        self.model.to(self.device)

    def predict(self, **inputs: Dict[str, Any]):
        """Runs a forward pass with the given inputs.

        Input format: {"input_strings": ["<instruction>", "<sentence>"]}
        """
        if 'input_strings' not in inputs:
            raise KeyError('input_strings key not in inputs')

        embeddings = self.model.encode(inputs['input_strings'])
        return embeddings.tolist()
