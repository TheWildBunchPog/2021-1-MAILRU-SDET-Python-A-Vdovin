import pytest
from api.client import ApiClient


class TestApi:
    client = ApiClient()

    @pytest.mark.API
    def test_create_and_delete_campaign(self):
        name = "Test campaign"
        campaign_id = self.client.post_create_campaign(name)
        assert campaign_id in self.client.get_check_campaign()
        self.client.delete_campaign(campaign_id)
        assert campaign_id not in self.client.get_check_campaign()

    @pytest.mark.API
    def test_create_segment(self):
        name = "Test segment"
        segment_id = self.client.post_create_segment(name)
        assert segment_id in self.client.get_check_segment()
        self.client.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        name = "Test segment"
        segment_id = self.client.post_create_segment(name)
        self.client.delete_segment(segment_id)
        assert segment_id not in self.client.get_check_segment()
