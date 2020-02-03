import thorpy

application = thorpy.Application(size=(300,300), caption="Hello Test")

my_button = thorpy.make_button("hello there")
my_button.center()

menu = thorpy.Menu(my_button)
menu.play()

application.quit()