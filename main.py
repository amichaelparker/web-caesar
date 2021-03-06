#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import webapp2
import caesar

def build_page(textarea_content):
    '''
    Build core document page
    '''

    title = '<head><title>Web Caesar</title></head>'
    header = '<h2>Web Caesar</h2>'

    rot_label = '<label style="margin-right: 44px">Rotate by:</label>'
    rotation_input = '<input name="rotation"/>'

    message_label = '<label>Type a message: </label>'
    textarea = ('<textarea name="message" \
                style="height: 100px; width: 300px; resize: none">' +
                textarea_content + '</textarea>')

    submit = '<input type="submit"/>'
    form = ('<form method="post">' +
            rot_label + rotation_input + '<br>' +
            '<br>' + message_label + textarea + '<br>' +
            '<br>' + submit + '</form>')

    return title + header + form

class MainHandler(webapp2.RequestHandler):
    '''
    Main page handler class for GAE
    '''

    def get(self):
        '''
        GET function for main page
        '''

        content = build_page("")

        self.response.write(content)

    def post(self):
        '''
        POST function for sending message to encrypt
        '''

        message = self.request.get("message")
        rotation = self.request.get("rotation")

        if rotation.isdigit():
            encrypted_message = caesar.encrypt(message, int(rotation))
        else:
            encrypted_message = caesar.encrypt(message, 0)

        encrypted_message = cgi.escape(encrypted_message)
        content = build_page(encrypted_message)

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
