@staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares using turtle."""
        import turtle

        t = turtle.Turtle()
        t.screen.title("Rectangles and Squares")
        t.pensize(3)

        # Draw all Rectangles
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.fillcolor("cyan")
            t.begin_fill()
            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)
            t.end_fill()

        # Draw all Squares
        for sq in list_squares:
            t.penup()
            t.goto(sq.x, sq.y)
            t.pendown()
            t.fillcolor("magenta")
            t.begin_fill()
            for _ in range(2):
                t.forward(sq.width)
                t.right(90)
                t.forward(sq.height)
                t.right(90)
            t.end_fill()

        turtle.done()
