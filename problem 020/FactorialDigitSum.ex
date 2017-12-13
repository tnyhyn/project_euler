defmodule Re do

  def main(x) do
    y = factorial(x) |> Integer.to_string() |> String.codepoints()
    acc({y,0})
  end

  defp acc(x) do
    if elem(x,0) == [] do elem(x,1)
    else
      [h|t] = elem(x,0)
      acc = elem(x,1) + String.to_integer(h)
      acc({t,acc})
     end
  end

  def factorial(x) do
    if x == 1 do x
    else x * factorial(x - 1) end
  end

end
