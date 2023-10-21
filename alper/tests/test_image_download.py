from bing_image_downloader import downloader

query_string = "8-bit plate"
d = downloader.download(query_string, 
                    limit=100, 
                    output_dir='dataset', 
                    adult_filter_off=True, 
                    force_replace=False, 
                    timeout=60, 
                    verbose=True)
