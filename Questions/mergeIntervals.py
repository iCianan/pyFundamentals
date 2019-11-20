def merge(intervals):
    if len(intervals) == 1:
        return intervals
    output = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if output and i[0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1], i[1])
        else:
            output += i,
    return output  

    

def main():
    collections = [[1,3],[2,6],[8,10],[15,16]]
    print(merge(collections))


if __name__ == "__main__":
    main()