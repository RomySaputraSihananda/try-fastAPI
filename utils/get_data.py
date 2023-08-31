import json;

def get_data(category, page):

    try:
        
        path = f'data/{category}/all_page.json' if(not page) else f'data/{category}/page_{page}/page_{page}.json';

        with open(path, 'r') as file:
            data = file.read();
            
            return [json.loads(data), f'data category {category} {"all Data" if(not page) else f"page-{page}"}'];
    
    except:

        return [[], 'data tidak ada'];