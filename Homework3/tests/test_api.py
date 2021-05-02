import pytest
from api.client import ApiClient
from base import ApiBase


class CampaignBase(ApiBase):
    client = ApiClient()

    def check_campaign(self):
        all_campaigns = self.client.get_all_campaign()
        return [response['id'] for response in all_campaigns['items']]


class SegmentBase(ApiBase):
    client = ApiClient()

    def check_segment(self):
        all_segment = self.client.get_all_segment()
        return [response['id'] for response in all_segment['items']]


class TestCampaign(CampaignBase):

    @pytest.mark.API
    def test_create_and_delete_campaign(self):
        campaign_data = self.builder.create_campaign()
        campaign_id = self.client.post_create_campaign(name=campaign_data.name_campaign)
        assert campaign_id in self.check_campaign()
        self.client.delete_campaign(campaign_id)
        assert campaign_id not in self.check_campaign()


class TestSegment(SegmentBase):

    @pytest.mark.API
    def test_create_segment(self):
        segment_data = self.builder.create_segment()
        segment_id = self.client.post_create_segment(name=segment_data.name_segment)
        assert segment_id in self.check_segment()
        self.client.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        segment_data = self.builder.create_segment()
        segment_id = self.client.post_create_segment(name=segment_data.name_segment)
        self.client.delete_segment(segment_id)
        assert segment_id not in self.check_segment()
