from flask import Flask, render_template, request, send_from_directory
from flask_caching import Cache

import scraper
input_url = 'https://12factor.net/'

app = Flask(__name__)
# Configuration for Flask-Caching
app.config['CACHE_TYPE'] = 'simple'  # Use simple in-memory caching
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache timeout in seconds (e.g., 300 seconds = 5 minutes)

cache = Cache(app)





@app.route('/')
@cache.cached()  # Cache the result of this view function
def index():
    header_data = scraper.getting_header_info(input_url)
    main_content = scraper.getting_chapter_main_content(input_url)
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/about')
@cache.cached()  # Cache the result of this view function
def about():
    header_data = scraper.getting_header_info(input_url)
    footer_data = scraper.getting_footer_info(input_url)
    return render_template('about.html', header = header_data, context = footer_data)


@app.route('/chapters')
@cache.cached()  # Cache the result of this view function
def chapters():
    header_data = scraper.getting_header_info(input_url)
    chapters = scraper.getting_chapters(input_url)
    return render_template('chapters.html', header = header_data, chapters = chapters)

@app.route('/<path:filename>')
def get_pictures(filename):
    return send_from_directory('static', filename)


@app.route('/langs')
@cache.cached()  # Cache the result of this view function
def languages():
    header_data = scraper.getting_header_info(input_url)
    footer_data = scraper.getting_footer_info(input_url)
    return render_template('languages.html', header = header_data, footer_data = footer_data)

# routes for chapters ...

@app.route('/codebase')
@cache.cached()  # Cache the result of this view function
def codebase():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/dependencies')
@cache.cached()  # Cache the result of this view function
def dependencies():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/config')
@cache.cached()  # Cache the result of this view function
def config():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/backing-services')
@cache.cached()  # Cache the result of this view function
def backingServices():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/build-release-run')
@cache.cached()  # Cache the result of this view function
def buildReleaseRun():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/processes')
@cache.cached()  # Cache the result of this view function
def processes():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/port-binding')
@cache.cached()  # Cache the result of this view function
def portBinding():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)


@app.route('/concurrency')
@cache.cached()  # Cache the result of this view function
def concurrency():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/disposability')
@cache.cached()  # Cache the result of this view function
def disposability():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)



@app.route('/dev-prod-parity')
@cache.cached()  # Cache the result of this view function
def devProtParity():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/logs')
@cache.cached()  # Cache the result of this view function
def logs():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)

@app.route('/admin-processes')
@cache.cached()  # Cache the result of this view function
def adminProcesses():
    header_data = scraper.getting_header_info(input_url)
    route_path = request.path
    new_input_url = input_url[:-1] + route_path
    main_content = scraper.getting_chapter_main_content(new_input_url) 
    return render_template('index.html', header = header_data, content = main_content)



if __name__ == '__main__':
    app.run(debug=True)


