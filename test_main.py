import main

def test_main(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from AGAJ!\n"
