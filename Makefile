.PHONY: build rebuild journal_reader clean

dist = ./
src_to_reader = src/journal_reader.py

build: journal_reader

rebuild: build clean

journal_reader:
	@echo "Start building"
	poetry run pyinstaller --onefile --name journal_reader --distpath $(dist) --workpath build --specpath build $(src_to_reader)
	rm -rf build *.spec
	@echo "End building"

test: test_journal_reader

test_journal_reader:
	poetry run python test/journal_reader_test.py

clean:
	rm -rf build journal_reader *.spec
