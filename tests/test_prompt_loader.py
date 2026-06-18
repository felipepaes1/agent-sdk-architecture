from summit_agents.prompts import load_prompt


def test_load_prompt_substitutes_variables(tmp_path):
    prompt = tmp_path / "hello.md"
    prompt.write_text("Hello $name", encoding="utf-8")

    assert load_prompt("hello", {"name": "Ada"}, prompts_dir=tmp_path) == "Hello Ada"


def test_load_prompt_keeps_unknown_variables(tmp_path):
    prompt = tmp_path / "hello.md"
    prompt.write_text("Hello $name from $place", encoding="utf-8")

    assert load_prompt("hello", {"name": "Ada"}, prompts_dir=tmp_path) == "Hello Ada from $place"
