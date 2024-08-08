import mitmproxy.http
import json
import os

class CaptureInfoWriteFile:
    def __init__(self):
        path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        self.history_file = path + '/Data/request2.json'  # 指定歷史請求檔名
        self.static_ext = ['js', 'css', 'ico', 'jpg', 'png', 'gif', 'jpeg', 'bmp', 'conf', 'html']

        # 如果歷史請求文件不存在，則建立一個空文件
        if not os.path.exists(self.history_file):
            with open(self.history_file, 'w', encoding='utf-8') as history_file:
                history_file.write('[]')

    def request(self, flow: mitmproxy.http.HTTPFlow):
        flow_request = flow.request
        url = flow_request.url
        path = flow_request.path.split('?')[0]
        if path == "/":
            return
        method = flow_request.method
        if method == "GET":
            query = flow_request.query
            text = "&".join([f"{param_name}={param_value}" for param_name, param_value in query.items()])
        else:
            text = flow_request.text
        last_path = url.split('?')[0].split('/')[-1]
        
        if flow_request.host != "api.adapt.chat":
            return
        
        if last_path.split('.')[-1] in self.static_ext:
            return
        
        #if not text:
        #    return
        
        # 讀取歷史請求文件
        with open(self.history_file, 'r', encoding='utf-8') as history_file:
            history_data = json.load(history_file)
        
        # 檢查是否存在具有相同路徑和方法的條目
        for item in history_data:
            if item['path'] == path and item['method'] == method:
                # 合併請求文本到現有條目
                item['request_text'] = self._merge_request_text(item['request_text'], text)
                break
        else:
            # 如果不存在，則新增條目
            data = {
                'path': path,
                'method': method,
                'request_text': text
            }
            history_data.append(data)
        
        # 寫入歷史請求文件
        with open(self.history_file, 'w', encoding='utf-8') as history_file:
            json.dump(history_data, history_file, indent=2, ensure_ascii=False)
    
    def _merge_request_text(self, existing_text, new_text):
        try:
            existing_data = json.loads(existing_text)
            new_data = json.loads(new_text)
            if isinstance(existing_data, list):
                if isinstance(new_data, list):
                    return json.dumps(existing_data + new_data)
                else:
                    existing_data.append(new_data)
                    return json.dumps(existing_data)
            else:
                if isinstance(new_data, list):
                    new_data.append(existing_data)
                    return json.dumps(new_data)
                else:
                    return json.dumps([existing_data, new_data])
        except json.JSONDecodeError:
            # 如果現有文字不是JSON格式，則將新文字作為單獨的請求儲存
            return existing_text + '\n' + new_text
        
    
addons = [CaptureInfoWriteFile()]
