from flask import Flask, render_template
import speedtest

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test")
def run_speed_test():
    try:
        st = speedtest.Speedtest()

        download = st.download() / 1000000
        upload = st.upload() / 1000000

        st.get_servers([])
        ping = st.results.ping

        return render_template(
            "index.html",
            download=round(download, 3),
            upload=round(upload, 3),
            ping=round(ping, 2)
        )

    except Exception as e:
        return render_template(
            "index.html",
            error="Speed test failed: " + str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)
