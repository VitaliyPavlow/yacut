from datetime import datetime
from . import db, Config


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original, short_link=Config.BASE_LINK + self.short
        )

    def from_dict(self, data):
        self.original = data["url"]
        if "custom_id" in data:
            self.short = data["custom_id"]


# db.drop_all()
db.create_all()
