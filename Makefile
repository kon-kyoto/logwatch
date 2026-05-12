.PHONY: build clean

dist = ./
src_to_reader = src/journal_reader.py

build:
	@echo "Start building"
	poetry run pyinstaller --onefile --name journal_reader --distpath $(dist) --workpath build --specpath build $(src_to_reader)
	@echo "End building"

clean:
	rm -rf build journal_reader *.spec
