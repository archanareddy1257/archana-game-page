class TicTacToe:
    def __init__(self) -> None:
        self.x = set()
        self.o = set()
        self.win = (
            {1, 2, 3},
            {1, 5, 9},
            {1, 4, 7},
            {2, 5, 8},
            {3, 5, 7},
            {3, 6, 9},
            {4, 5, 6},
            {7, 8, 9},
        )

    def __str__(self) -> str:
        k = 15
        space = "   "
        s = "=" * (k // 3) + "BOARD" + "=" * (k // 3) + "\n"
        p = 1
        for i in range(0, 3):
            s += "  "
            for j in range(0, 3):
                if p in self.x:
                    s += "X" + space
                elif p in self.o:
                    s += "O" + space
                else:
                    s += "_" + space
                p += 1
            s += "\n"
        s += "=" * k
        return s

    def generateBoard(self) -> dict:
        board = {}
        p = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if p in self.x:
                    board[p] = "X"
                elif p in self.o:
                    board[p] = "O"
                else:
                    board[p] = ""
                p += 1

        return board

    def inp_parser(self, turn):
        try:
            inp = int(input((f"Enter Input for PLAYER {turn %2 + 1} : ")))
            if (inp > 0 and inp < 10) and not (inp in self.x or inp in self.o):
                self.add_inp(turn, inp)
            elif not (inp > 0 and inp < 10):
                print("valid range for input : [1,9] inclusive")
                raise Exception
            elif inp in self.x:
                print("Input is already taken by PLAYER 1")
                raise Exception
            elif inp in self.o:
                print("Input is already taken by PLAYER 2")
                raise Exception
            else:
                raise Exception
        except Exception:
            print("INVALID INPUT")
            self.inp_parser(turn)
        # finally:
        #     return inp

    def inp_parser_web(self, turn, inp):
        if not (inp in self.x or inp in self.o):
            self.add_inp(turn, inp)
        elif inp in self.x:
            return "Input is already taken by PLAYER X"
        elif inp in self.o:
            return "Input is already taken by PLAYER O"
        return None

    def add_inp(self, turn, inp):
        if turn % 2 == 0:
            self.x.add(inp)
        elif turn % 2 == 1:
            self.o.add(inp)

    def result(self):
        for i in self.win:
            if self.x.issuperset(i):
                print("\n" + ("$" * 30) + "\n\n\tPLAYER 1 WON \n\n" + ("$" * 30))
                return "X"
            elif self.o.issuperset(i):
                print("\n" + ("$" * 30) + "\n\n\tPLAYER 2 WON \n\n" + ("$" * 30))
                return "O"
        else:
            if len(self.x) == 5 and len(self.o) == 4:
                print("\n" + ("$" * 30) + "\n\n\tIT's A DRAW \n\n" + ("$" * 30))
                return "DRAW"
            else:
                return None


class webGameTicTacToe:
    def __init__(self) -> None:
        self.Game = TicTacToe()
        self.turn = 0
        self.loops = 10

    def gameForwardStep(self, inp=None):
        result = {
            "winner": None,  # X , O , DRAW
            "status": "NotStarted",  # GameOver , Playing
            "turn": "X",  # init X then O
            "board": self.Game.generateBoard(),
            "message": "",
        }

        if inp:
            validated = self.Game.inp_parser_web(self.turn, inp)
            if validated:
                result["message"] = validated
            else:
                if self.turn % 2 == 0:
                    result["turn"] = "O"
                else:
                    result["turn"] = "X"
                res = self.Game.result()
                self.loops -= 1
                self.turn += 1
                if res != None:
                    result["status"] = "GameOver"
                    result["winner"] = res
            result["board"] = self.Game.generateBoard()

        return result

    def reset(self):
        self.Game = TicTacToe()
        self.turn = 0
        self.loops = 10


def main():
    Game = TicTacToe()
    print(
        """Enter the digits in between 1 to 9 to mark your marker\n\t1\t2\t3\n\t4\t5\t6\n\t7\t8\t9\n"""
    )
    print(Game)
    turn = 0
    Loops = 10
    while Loops:
        Game.inp_parser(turn)
        print(Game)
        res = Game.result()
        if res != None:
            print("GAME OVER")
            break
        Loops -= 1
        turn += 1


if __name__ == "__main__":
    while 1:
        main()
        again = input("\n\nPRESS Y to PLAY AGAIN : ")
        if again not in ("Y", "y", "YES", 1):
            break
    print("BYE !")
