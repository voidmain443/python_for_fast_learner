{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Math with code1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyN+VS7LkwHw1PyKqC8JgPpB"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "deep copy"
      ],
      "metadata": {
        "id": "G4_EmLkrPzmu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=[1,2,3,4]"
      ],
      "metadata": {
        "id": "bJnTY2qSyElb"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "id(a)"
      ],
      "metadata": {
        "id": "NVqjwFuUyEis",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "53fb19eb-8977-48d5-f050-908221aef310"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "140562443526864"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a))\n",
        "print(id(a[0]))\n"
      ],
      "metadata": {
        "id": "sHrYfjGwyEfc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "63e76487-aa1b-4b53-b4d4-c6a6f0807e4f"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562443526864\n",
            "94409736133120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a[0]= 5"
      ],
      "metadata": {
        "id": "h2DtIM-MQ-jZ"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "id(a[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yI_Js9dWRDPk",
        "outputId": "f9eeff96-59d6-4dc8-9de6-7e372062f5f0"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "94409736133248"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "VTJTFQfuROC_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "list is mutable and the element is immutable"
      ],
      "metadata": {
        "id": "AfHkCfJWQrWO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "b =a \n",
        "print(b)"
      ],
      "metadata": {
        "id": "fehS2mutyEZc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "79da4caa-c6ba-4fb3-a072-332aeaf960c8"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a))\n",
        "print(id(b))"
      ],
      "metadata": {
        "id": "g0w0bKrpyEWv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d120e1f7-28df-4a62-d93f-53dc84d739f9"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562443526864\n",
            "140562443526864\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0]))\n",
        "print(id(b[0]))"
      ],
      "metadata": {
        "id": "McOq-ZS8yETm",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4a936e34-6ae3-43c0-c0fd-48c5990e6540"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "94409736133248\n",
            "94409736133248\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "b.append(7)"
      ],
      "metadata": {
        "id": "xHRi0jUXyEQf"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(a)\n",
        "print(b)"
      ],
      "metadata": {
        "id": "buQJVEmPyENX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fbd9c7e5-429e-48ae-99c6-99766ceb2210"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 2, 3, 4, 7]\n",
            "[5, 2, 3, 4, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "we have to deal with \"copy\""
      ],
      "metadata": {
        "id": "NkPnfDVtRqmx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = [1,2,3,4,5]\n",
        "b = a[:]"
      ],
      "metadata": {
        "id": "OAghjxhfyEJ_"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a))\n",
        "print(id(b))\n",
        "#shallow copy"
      ],
      "metadata": {
        "id": "PeWaz3DTyEGo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1f786118-9c14-4a7a-b5db-2d1a50816dba"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562443497712\n",
            "140562442994624\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# the element is immutable as it be \n",
        "print(id(a[0]))\n",
        "print(id(b[0]))"
      ],
      "metadata": {
        "id": "KuD98tQmyECn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ed039cc3-c96b-48f1-9626-9a766df81b41"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "94409736133120\n",
            "94409736133120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "b[0] = 9\n",
        "print(b)"
      ],
      "metadata": {
        "id": "zE2p0rNjyD-E",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "099f5ddd-ab61-4bca-cc3c-b73716392563"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[9, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a)"
      ],
      "metadata": {
        "id": "-j75Zf79yD4i",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8862134f-19dc-4314-e41c-aadae516ebc3"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import copy\n",
        "\n",
        "a=[1,2,3,4,5]\n",
        "b = copy.copy(a)"
      ],
      "metadata": {
        "id": "yhWGL-NsyDpE"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a))\n",
        "print(id(b))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zMpcQx_dSR8R",
        "outputId": "f9620e54-ebe9-4531-b70c-3e37acf8bd12"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562443319328\n",
            "140562443377712\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#shallow copy is usefull if the mutable object structured by immutable object \n",
        "# but what if the opposite side ?\n",
        "\n",
        "a = [[1,3],[2,4]]\n",
        "b=copy.copy(a)\n",
        "print(a)\n",
        "print(b)\n",
        "print(id(a))\n",
        "print(id(b))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hpBDDctWSR5B",
        "outputId": "3dd5aff1-572c-432c-f136-fe388fa47707"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 3], [2, 4]]\n",
            "[[1, 3], [2, 4]]\n",
            "140562443307600\n",
            "140562442812544\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0]))\n",
        "print(id(b[0]))\n",
        "print(id(a[0][0]))\n",
        "print(id(b[0][0]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7Satnl_ESR2F",
        "outputId": "35695b98-2bc7-4a2a-e589-1633c2d71658"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562442790464\n",
            "140562442790464\n",
            "94409736133120\n",
            "94409736133120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "b[0][0]=7\n",
        "print(b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VjvA49UZSRyp",
        "outputId": "21795805-bac2-4b63-9fce-8a5ef28d30ee"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[7, 3], [2, 4]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oMM-aURSSRvq",
        "outputId": "695350d7-5de8-4a9b-a593-1676874b00af"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[7, 3], [2, 4]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0]))\n",
        "print(id(b[0]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5FXbn1TrSRsr",
        "outputId": "8c593991-f408-4aef-9309-a8ad6221f882"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562442790464\n",
            "140562442790464\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0][0]))\n",
        "print(id(b[0][0]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0kCKGcn1WWwM",
        "outputId": "dcc75315-ae4d-410e-ee70-68930348554d"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "94409736133312\n",
            "94409736133312\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "shallow copy don't solve the problam that mutable object inside the mutable object. it change the mutable list in same time."
      ],
      "metadata": {
        "id": "FrEq-rdGWow_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# deep copy \n",
        "a=[[1,2],[3,4]]\n",
        "b= copy.deepcopy(a)"
      ],
      "metadata": {
        "id": "66n_dmKfWWq3"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(a)\n",
        "print(b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ACxAn6zPWWj1",
        "outputId": "8d123550-574e-4eb1-d84e-2bf1dfeb352f"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2], [3, 4]]\n",
            "[[1, 2], [3, 4]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a))\n",
        "print(id(b))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wqnbKxyyWWdm",
        "outputId": "4183c8c9-7c05-4737-df33-f1211f600def"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562442894384\n",
            "140562513580512\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0]))\n",
        "print(id(b[0]))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TBr8zgSZWWW4",
        "outputId": "27d509a4-1d32-4cb4-da5d-bac43aa6e37e"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140562442867968\n",
            "140562443440208\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0][0]))\n",
        "print(id(b[0][0]))\n",
        "# it is same in here"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "teICWJG4WWQJ",
        "outputId": "f67309f7-672a-41b4-c639-2ad089b65cc9"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "94409736133120\n",
            "94409736133120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "b[0][0] =7 \n",
        "print(b)\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O0r6zy8CWWGJ",
        "outputId": "bbff478c-71ed-440e-cf58-115fa7aecc2c"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[7, 2], [3, 4]]\n",
            "[[1, 2], [3, 4]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(id(a[0][0]))\n",
        "print(id(b[0][0]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D2yJBduxSRpV",
        "outputId": "2972b08b-72f3-4b74-cddd-29beee34b21a"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "94409736133120\n",
            "94409736133312\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def zero_mat(n,p):\n",
        "  \"\"\"\n",
        "  zero matrix \n",
        "  input: n x p size\n",
        "  output: (n x p) zero matrix Z \n",
        "  \"\"\"\n",
        "  Z =[]\n",
        "  for i in range(0,n):\n",
        "    row =[]\n",
        "    for j in range(0,p):\n",
        "      row.append(0)\n",
        "    Z.append(row)\n",
        "  return Z"
      ],
      "metadata": {
        "id": "hL2UxwspbUKK"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def deepcopy(A):\n",
        "  \"\"\"\n",
        "  deepcopy \n",
        "  input: matrix list A\n",
        "  output : deepcopyed matrix list res\n",
        "  \"\"\"\n",
        "  if type(A[0]) == list:\n",
        "    n =len(A)\n",
        "    p = len(A[0])\n",
        "    res = zero_mat(n,p)\n",
        "    for i in range(0,n):\n",
        "      for j in range(0,p):\n",
        "        res[i][j]= A[i][j]\n",
        "    return res\n",
        "  else:\n",
        "    n =len(A)\n",
        "    res =[]\n",
        "    for i in range(0,n):\n",
        "      res.append(A[i])\n",
        "    return res"
      ],
      "metadata": {
        "id": "9EgDvWHVSRlr"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "A = [[1,2,3],[4,5,6],[7,8,9]]\n",
        "B = deepcopy(A)\n",
        "print(B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8lAFGK4HSRiv",
        "outputId": "08b00b4c-7167-47ce-ce08-c8d330509769"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = [1,2,3]\n",
        "b=deepcopy(a)\n",
        "b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "siy25FPEciOh",
        "outputId": "c4cb9e9a-ac55-4b83-b188-d0bcf8869f2a"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3]"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "CuWOMmuOcf_8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# math with code \n",
        "----\n",
        "invent the game: start playing with some mathematical objects\n",
        "\n",
        "form some conjectures: speculate about  some general facts you dcan state about your game, and at least convince yourself they must be true.\n",
        "\n",
        "develop some precise language to describe your game and your conjectures. your confectures won't mean anything until you can communicate them.\n",
        "\n",
        "finally with some determination and luck , find a proof for your conjecture, showing why it needs to be true. \n",
        "---\n",
        "\n",
        "there is a math module \n",
        "\n",
        "## Building abstractions with functions\n",
        "\n",
        "the process  describe is called \"abstraction\"\n",
        "\n"
      ],
      "metadata": {
        "id": "AghNeU1DHpjl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Drawing with 2D vectors \n",
        "---\n",
        "Creating and manipulating 2D drawings as collections of vectors\n",
        "\n",
        "thinking of 2D vectors as arrows locations and ordered pairs of coordinates.\n",
        "\n",
        "Using vector arithmetic to transform shapes in the plane.\n",
        "\n",
        "Using trigonometry to measure distances and angles in the plane . \n",
        "\n",
        "Vectors are objects that live in multi-dimentional spaces. \n",
        "arithmetric (adding, multiplying and s on)\n",
        "\n",
        "\n",
        "The locations in 2D can be described two pieces of infomation: their vertical and horizontal positions.\n",
        "\n",
        "to describe the location of point in the plane , we need a referencepoint. \n",
        "\n",
        "we call that special reference point the origin.\n",
        "\n",
        "horizontal axis is call the x-axis\n",
        "vertical axis is called the y-axis\n",
        "\n",
        "|class|constructor example|description|\n",
        "----|-----|-----\n",
        "|polygon|polygon(*vectors)|a polygon whose vertices (corners) are represented by a list of vectors.|\n",
        "|Points|Points(*vectors)| Represents a list of point (dots) to draw, one at each of the input vectors.|\n",
        "|Arrow|Arrow(tip)<br> Arrow(tip,tail) | Draaws an arrow from the origin to the tip vector,or from that tail vector to the head vector if a tail is specified.|\n",
        "|segement| segement(start,end)| Draws a line segement from the start tothe vector end.|\n",
        "\n"
      ],
      "metadata": {
        "id": "Fj192yQZpR4A"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 405
        },
        "id": "ZrsG-z4NHmBZ",
        "outputId": "12ecec20-5faf-433b-ce4d-704d63c8fef1"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-114f61b35257>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mvector_drawing\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mdino_vectors\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'vector_drawing'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "from vector_drawing import *\n",
        "dino_vectors = [(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),]"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "math "
      ],
      "metadata": {
        "id": "2WYEIB3UvAly"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}