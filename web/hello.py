def app(env, start_response):
	query_string = env.get('QUERY_STRING', '')
	data = '\n'.join(query_string.split('&'))
	start_response("200 OK", [("Content-Type", "text/plain")])
	return iter([data.encode()])
