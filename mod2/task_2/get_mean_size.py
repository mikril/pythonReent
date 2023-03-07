import sys
def get_mean_size(data):
    sum=0
    lines=data.readlines()[1:]
    for line in lines:
        sum+=int(line.split()[4])
    get_summary_rss(sum/len(lines))
def get_summary_rss(number):
    sizes = ["B", "KiB", "MiB", "GiB"]
    counter = 0

    result = f"{round(number, 3)} {sizes[counter]}"

    while (number // 1024 != 0):
        number = number / 1024
        counter += 1
        result = f"{round(number, 3)} {sizes[counter]}"

    print(result)

if __name__ =="__main__":
    get_mean_size(sys.stdin)