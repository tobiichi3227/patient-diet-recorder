# Changelog

## Patient Intake/Output Recorder

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
