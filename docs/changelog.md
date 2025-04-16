# Changelog

## Patient Intake/Output Recorder

### 1.2.0 <small>April 16, 2025</small> { id="1.2.0" }

**Features**

- **Monitor**: Transfer patient data between accounts with validation and confirmation (#54)
- **Monitor**: Clear all data from a monitored patient with confirmation (#53)
- **Monitor**: Add copy and print QR Code buttons with proper preview and validation (#47, #49)
- **Signup**: Add options to keep signup modal open and auto-add patient to monitor list (#68, #70)
- **API**: Introduce unit tests for API and database (#15)
- **API**: Add support for changing monitor account name and password (#56, #57)
- **Signup**: Persist signup modal preferences using localStorage

**Improvements**

- **UI**: Improve responsive layout of monitor header bar (#63)
- **Alert/Confirm**: Replace native `alert()` and `confirm()` with Bootstrap-styled alternatives (#51, #81)
- **UX**: Show patient username above QR code in print preview
- **Accessibility**: Align patient button actions with stable patient keys (replace index)
- **Performance**: Reduce monitor sync bandwidth by syncing only when tab is visible
- **Refactor**: Debounce search without using lodash (#73)
- **Maintainability**: Reorder Vue options for consistency

**Fixes**

- Prevent transfer to target with existing data or unmonitored account
- Improve empty data check using filtered key comparison
- Correct patient list UI updates after deletion
- Add missing permission checks and token validation in API
- Fix z-index of time block overlapping header buttons (#48)
- Fix grammatical and logic issues in API

**Documentation**

- Add supported languages to `README.md`
- Update `CONTRIBUTING.md` with new confirm modal translation keys

**CI / Infrastructure**

- Add file-filtering to GitHub Pages deploy
- Run unit tests in CI for backend
- Upgrade GitHub Action workflows and dependencies

**Chores**

- Update project logo and favicons
- Run `poetry update && poetry export`
- Bump dependencies: Jinja2, Starlette
- Update copyright

### 1.1.0 <small>November 10, 2024</small> { id="1.1.0" }

**Added:**

- **Documentation Setup:** Set up the documentation website with MkDocs Material, including basic structure and enhanced installation/configuration instructions (Closes #58).
- **Documentation Improvements:** Added a CONTRIBUTING guide and GPL-3.0 License in `docs/` directory.
- **Signup Alerts:** Enhanced signup alerts with Bootstrap styles and modals for improved UI consistency.
- **Account Management:** Display account name beside the logout button for quick reference.
- **Navigation Buttons:** Added arrow icons to navigation buttons and a new "Documentation" button on the home page for enhanced user guidance.

**Changed:**

- **Icon Library Update:** Replaced all Material Symbols with FontAwesome icons and updated icon classes from 'fas' to 'fa-solid' for improved icon consistency.
- **Responsive Design:** Wrapped tables in `table-responsive` to prevent overflow in accordions, enhancing mobile experience.
- **External Libraries CDN:** Updated external libraries to Cloudflare CDN with integrity hashes for improved loading speed and security.
- **URL Configuration:** Replaced hardcoded web and API URLs with dynamic configurations for more flexible environment setups.
- **Button Styling:** Converted patient and monitor links to buttons with `onclick` navigation for a more intuitive interface.

**Fixed:**

- **Login Validation:** Enforced validation to prevent whitespace-only account names (Closes #66).
- **QR Code Error:** Fixed QR code length overflow error to prevent unexpected application behavior (Closes #69).
- **Monitor Settings:** Enforced positive integer input for patient limit amount, ensuring reliable patient record handling.
- **Styling Issues:** Resolved UI inconsistencies, including login page eye icon border and header layout for manage and signup buttons.

**Documentation:**

- **Getting Started Guide:** Updated configuration setup instructions and enhanced guidance using MkDocs Material elements.
- **README Updates:** Expanded documentation links and clarified setup details for both frontend and backend configurations.

**CI/CD:**

- **GitHub Deployment Workflow:** Added `gh-deploy.yml` for deploying the documentation site via GitHub Pages.
- **CI Optimization:** Removed unused `.github/workflows/static.yml` to streamline CI.

### 1.0.0 <small>October 22, 2024</small> { id="1.0.0" }

Patient Intake/Output Recorder v1.0.0 is now live, designed to streamline patient dietary tracking in hospitals and nurse centers. This release automates recording and monitoring patient intake (food, water) and output (urination, defecation), providing accurate and real-time data synchronization between patients and monitors.

**Key Features:**

- Two-Sided Interface: Separate views for patients and monitors, enabling seamless daily intake and output tracking.
- Data Synchronization: Automatically sums and syncs data, making it easy for both patients and monitors to stay updated.
- Restriction Management: The monitor side can set custom daily intake limits for food and water, with warnings to keep patients within healthy boundaries.
- Weight Tracking: Patients can record their weight as part of the health monitoring process.
- History Tracking: All records are saved, allowing patients and monitors to view the history of dietary records and monitor progress over time.

**Tech Stack:**

- Backend: FastAPI and Uvicorn.
- Frontend: Vue and Bootstrap 5.

**Documentation:**

- Documentation is currently being developed and will be available soon.

**Development Status:**

- The project is still in active development with several open issues, and we welcome contributions from the community. Whether you want to help with bug fixes, new features, or improvements, we'd love your support!
