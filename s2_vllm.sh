#! /bin/bash
python gui_agents/s2/cli_app.py --provider vllm \
--model google/gemma-3-4b-it \
--model_url http://localhost:8000/v1 \
--model_api_key vllm123 \
--grounding_model_provider vllm \
--grounding_model google/gemma-3-4b-it \