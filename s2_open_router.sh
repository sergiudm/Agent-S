#! /bin/bash
python gui_agents/s2/cli_app.py --provider open_router \
--model openai/gpt-4.1 \
--model_url "https://api.openrouter.ai/v1" \
--model_api_key "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" \
--grounding_model_provider open_router \
--grounding_model google/gemma-3-4b-it \