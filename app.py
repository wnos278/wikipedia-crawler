from src.crawler import * 
link_file = "link.txt"
# Flow 
seeds = get_seeds()
for seed in seeds: 
    while True:
        current_page = seed 
        # Start 
        raw_html = download_page(current_page)
        list_links = extract_list_data(raw_html)
        for link in list_links:
            with open(link_file, 'a') as log_f:
                log_f.write(f"{link}\n")
        # extract_data(list_links)
        next_page = extract_next_link(raw_html)
        print(next_page)
        if next_page: 
            seed = next_page
        else:
            print("xong page")
            break
            # print (web_crawl())

    # t1 = time.time()
    # total_time = t1-t0
    # print(total_time)