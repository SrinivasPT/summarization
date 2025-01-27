from graph import create_graph


def main():
    graph = create_graph("EDGE1004440")
    final_output = graph()

    # Print the final output
    print("Final Output:")
    print(final_output)


if __name__ == "__main__":
    main()
