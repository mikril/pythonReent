
def get_summary_rss(path):
    sumBait=0
    with open(path) as text:
        for line in text.readlines()[1:]:
            sumBait+=int(line.split()[5])
    sizes=["B","KiB","MiB","GiB"]
    counter=0
    number = sumBait
    result=f"{round(number,3)} {sizes[counter]}"

    while(number//1024!=0):
        number=number/1024
        counter+=1
        result=f"{round(number,3)} {sizes[counter]}"

    print(result)

if __name__ =="__main__":
    get_summary_rss("output_file.txt")

