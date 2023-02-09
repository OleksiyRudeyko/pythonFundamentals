x, y = input("Enter two values: ").split(', ')

print(f"X + Y = {int(x) + int(y)}\n",
      f"X - Y = {int(x) - int(y)}\n",
      f"X * Y = {int(x) * int(y)}\n",
      f"X / Y = {int(int(x) / int(y))}\n",
      f"X ** Y = {int(x) ** int(y)}\n",
      f"X // Y = {int(x) // int(y)}\n",
      f"X % Y = {int(x) % int(y)}", sep=""
      )
