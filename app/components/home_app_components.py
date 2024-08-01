import streamlit as st

from streamlit_lottie import st_lottie
from time import sleep

import streamlit as st
import os
from dotenv import load_dotenv
import json
import google.generativeai as genai

import base64
from PIL import Image
from io import BytesIO

load_dotenv()

from controller import LoginManager, SignupManager
from model import LottieManager
from ..s_state import LoggedinUserInfoSState, WakeupLottieSState, FinishedLoginLottieSState, LoggedinSState

class HomeAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Sereni Chat",
            # page_icon="🏠",
        )

    @staticmethod
    def init_session_state() -> None:
        LoggedinSState.init()
        WakeupLottieSState.init()
        FinishedLoginLottieSState.init()

    @staticmethod
    def wakeup_lottie() -> None:
        if not WakeupLottieSState.get():
            st_lottie(animation_source=LottieManager.WAKEUP_LOTTIE, key="WAKEUP_LOTTIE", speed=0.6, reverse=False, loop=False)
            sleep(1.3)
            WakeupLottieSState.set(value=True)
            st.rerun()
    
    @staticmethod
    def login_success_lottie() -> None:
        if not FinishedLoginLottieSState.get():
            st_lottie(animation_source=LottieManager.LOGIN_SUCCESS_LOTTIE, key="LOGIN_SUCCESS_LOTTIE", speed=1.7, reverse=False, loop=False)
            sleep(1.3)
            FinishedLoginLottieSState.set(value=True)
            st.rerun()
    
    @staticmethod
    def main_page() -> None:
        
        st.header(body="Sereni Chat", divider='blue')
        

        st.markdown(
            """
           Click on the sidebar to chat with the AI model.

            """,
            unsafe_allow_html=True
            
           
        )
        
        
        

        # st.write(f"Email: :[**{LoggedinUserInfoSState.get().username}**]")
    
    @staticmethod
    def signup_page() -> None:
        signup_form = st.form(key="signup_form")

        with signup_form:
            st.header(body=" Signup", divider='blue')
            username = st.text_input(label="👤 Email / Username", placeholder="Enter your Email / Username...")
            password = st.text_input(label="🔑 Password", type="password", placeholder="Enter your Password...")
            retype_password = st.text_input(label="✅ Confirm your Password", type="password", placeholder="Retype  Password...")
            submit_button = st.form_submit_button(label="Signup", type="primary")

        if submit_button:
            is_success, message = SignupManager.signup(username=username, password=password, retype_password=retype_password)
            
            with signup_form:
                if is_success:
                    st.success(icon="🙆", body=message)
                else:
                    st.warning(icon="🙅", body=message)

    @classmethod
    def login_page(cls) -> None:
        login_form = st.form(key="login_form")

        with login_form:
            st.header(body="🔒 Login", divider='blue')
            username = st.text_input(label="👤 Email / Username", placeholder="Enter your Email / Username...")
            password = st.text_input(label="🔑 Password", type="password", placeholder="Enter your Password...")
            submit_button = st.form_submit_button(label="Login", type="primary")

        if submit_button:
            is_success, message, user_info_instance = LoginManager.login(username=username, password=password)
            LoggedinSState.set(value=is_success)

            with login_form:
                if is_success:
                    st.success(icon="🎉", body=message)
                    LoggedinUserInfoSState.set(value=user_info_instance)
                    cls.login_success_lottie()
                else:
                    st.warning(icon="🙅", body=message)

            # st.rerun()

    @classmethod
    def select_signup_or_login_page(cls):
        signup_or_login =  st.radio(label="Kindly Login / Signup to continue", options=["**Login**", "**Signup**"], horizontal=True)
        if signup_or_login == "**Login**":
            cls.login_page()
        else:
            cls.signup_page()

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.wakeup_lottie()
        
        if LoggedinSState.get():
            
            
            cls.main_page()
        else:
            cls.select_signup_or_login_page()
            # cls.login_page()
