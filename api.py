import io
import requests
from typing import Optional

from fastapi import FastAPI, Header
from fastapi.responses import StreamingResponse
import cairosvg

app = FastAPI()

@app.get("/api/v1/svgpng")
async def convert_svg_to_png(svg_url: str, width: Optional[int] = 512, height: Optional[int] = 512, api_key: str = Header("X-API-KEY")):
    """
    Accepts an SVG URL, width, and height, and returns a PNG image.
    """
    if api_key != "b0e6a1c9a8d02d15dfe81e40462771f5436f3037f8eeb57ba47d7d489652631c":
        return {"error": "Invalid API key"}
    try:
        svg_bytes = requests.get(svg_url)
        if svg_bytes.status_code != 200:
            return {"error": "Invalid SVG URL"}
    except Exception as e:
        return {"error": str(e)}
    png_bytes = cairosvg.svg2png(bytestring=svg_bytes.content, output_width=width, output_height=height)
    
    return StreamingResponse(io.BytesIO(png_bytes), media_type="image/png")


app.debug = True
app.docs_url = "/docs"
app.contact = {
    "name": "KM. OZ.",
    "email": "contact@wepayme.com",
    "github": "https://github.com/KM8Oz",
    "linkedin": "https://www.linkedin.com/in/kmoz000",
    "twitter": "https://twitter.com/niceblueman",
}
app.license_info = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}
app.description = "convert an SVG file to a PNG file with a specified size"
app.title = "SVG to PNG"