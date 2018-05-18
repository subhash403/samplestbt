from menu import MainMenu


def test_ir_reliability():
    MainMenu.open()
    for _ in range(10):
        MainMenu().navigate_to("Search")
        MainMenu().navigate_to("Guide")
