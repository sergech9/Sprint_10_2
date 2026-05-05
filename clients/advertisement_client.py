from clients.base_client import BaseClient
from config import AD_PATH_TEMPLATE, ADS_PATH, DELETE_AD_PATH_TEMPLATE


class AdvertisementClient(BaseClient):
    def create_advertisement(self, payload, headers):
        return self.post(ADS_PATH, files=self._multipart_fields(payload), headers=headers)

    def edit_advertisement(self, ad_id, payload, headers):
        return self.patch(
            AD_PATH_TEMPLATE.format(ad_id=ad_id),
            files=self._multipart_fields(payload),
            headers=headers,
        )

    def delete_advertisement(self, ad_id, headers):
        return self.delete(DELETE_AD_PATH_TEMPLATE.format(ad_id=ad_id), headers=headers)

    @staticmethod
    def _multipart_fields(payload):
        return {key: (None, str(value)) for key, value in payload.items()}
