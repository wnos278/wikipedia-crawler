from src.crawler import * 




# Flow 
seeds = get_seeds() 
next_page = extract_next_link()
while next_page:
    current_page = next_page 

    # Start 
    raw_html = download_page(current_page)
    list_links = extract_list_data(raw_html)



    # Duy trì vòng lặp
    next_page = extract_next_link() 

print (web_crawl())

t1 = time.time()
total_time = t1-t0
print(total_time)