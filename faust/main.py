import faust

app = faust.App('page_views', broker='kafka://localhost:9092', value_serializer='raw')
page_views = app.topic('page_views')

@app.agent(page_views)
async def receive_change(change_logs):
    async for change in change_logs:
        print(change)