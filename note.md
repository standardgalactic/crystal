# Crystal Web Server (Serving Static Files)

This project uses a simple Crystal script (`python-server.cr`) to serve static files like HTML, CSS, and JS from a `public/` directory over HTTP.

## Requirements

- [Crystal](https://crystal-lang.org/install/) installed (v1.0+)
- Terminal access
- Files placed in the `public/` folder (e.g., `index.html`)

## Running the Server

1. Start the server from the root project directory:

   ```bash
   crystal run python-server.cr

