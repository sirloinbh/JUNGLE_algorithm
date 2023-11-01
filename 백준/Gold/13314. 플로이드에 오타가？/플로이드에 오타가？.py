def main():
    result = []
    result.append("100")
    for i in range(100):
        row = []
        for j in range(100):
            if i == j:
                row.append("0")
            elif j == 99 or i == 99:
                row.append("1")
            else:
                row.append("1000")
        result.append(" ".join(row))
    print("\n".join(result))

if __name__ == "__main__":
    main()
