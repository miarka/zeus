
from django.conf.urls import include, url
from zeus.views import poll, shared

poll_patterns = [
    url(r'^get-randomness$', shared.get_randomness),
]

poll_patterns += [
    url(r'^remove$', poll.remove, name='election_poll_remove'),
    url(r'^edit$', poll.add_edit, name='election_poll_edit'),
    url(r'^cast$', poll.cast, name='election_poll_cast'),
    url(r'^cast-done$', poll.cast_done, name='election_poll_cast_done'),
    url(r'^audited-ballot$', poll.audited_ballots,
        name='election_poll_audited_ballots'),
    url(r'^post-audited-ballot$', poll.post_audited_ballot,
        name='election_poll_post_audited_ballot'),
    url(r'^s/(?P<fingerprint>.*)$', poll.download_signature,
        name='election_poll_download_signature'),
    url(r'^questions$', poll.questions, name='election_poll_questions'),
    url(r'^questions/manage$', poll.questions_manage,
        name='election_poll_questions_manage'),
    url(r'^voters$', poll.voters_list,
        name='election_poll_voters'),
    url(r'^encrypted-tally$', poll.get_tally, name='election_poll_get_tally'),
    url(r'^post-decryptions$', poll.upload_decryption,
        name='election_poll_upload_decryption'),
    url(r'^voters/csv/(?P<fname>[^/]+).csv$', poll.voters_csv,
        name='election_poll_voters_csv'),
    url(r'^voters/clear$', poll.voters_clear, name='election_poll_voters_clear'),
    url(r'^voters/upload$', poll.voters_upload,
        name='election_poll_voters_upload'),
    url(r'^voters/upload-cancel$', poll.voters_upload_cancel,
        name='election_poll_voters_upload_cancel'),
    url(r'^voters/email$', poll.voters_email, name="election_poll_voters_email"),
    url(r'^voters/email/(?P<voter_uuid>[^/]+)$', poll.voters_email, name="election_poll_voter_email"),
    url(r'^voters/(?P<voter_uuid>[^/]+)/delete$', poll.voter_delete,
        name="election_poll_voter_delete"),
    url(r'^mix/(?P<mix_key>.*)$', poll.remote_mix, name="election_poll_remote_mix"),
    url(r'^voters/(?P<voter_uuid>[^/]+)/exclude$', poll.voter_exclude,
        name="election_poll_voter_exclude"),
    url(r'^l/(?P<voter_uuid>[^/]+)/linked-booth-login',
        poll.voter_booth_linked_login, name="election_poll_voter_booth_linked_login"),
    url(r'^results$', poll.results, name='election_poll_results'),
    url(r'^l/(?P<voter_uuid>[^/]+)/(?P<voter_secret>[^/]+)$',
        poll.voter_booth_login, name="election_poll_voter_booth_login"),
    url(r'^results$', poll.results, name='election_poll_results'),
    url(r'^results.json$', poll.results_json, name='election_poll_results_json'),
    url(r'^results-(?P<language>.*).pdf$', poll.results_file, name='election_poll_results_pdf',
        kwargs={'ext': 'pdf'}),
    url(r'^results-(?P<language>.*).csv$', poll.results_file, name='election_poll_results_csv',
        kwargs={'ext': 'csv'}),
    url(r'^proofs.zip$', poll.zeus_proofs, name='election_poll_zeus_proofs'),
    url(r'^sms_delivery$', poll.sms_delivery, name='election_poll_sms_delivery'),
]

urlpatterns = [
    url(r'^$', poll.polls_list, name='election_polls_list'),
    url(r'^add$', poll.add_edit, name='election_polls_add'),
    url(r'^(?P<poll_uuid>[^/]+)/', include(poll_patterns)),
    url(r'^(?P<poll_uuid>[^/]+).json', poll.to_json,
        name='election_poll_json'),
]
