FROM python:3.11-slim

# Rule E: Run Python in unbuffered mode
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Rule C: Create a non-root user to avoid local file permission conflicts
RUN useradd -m -u 1000 -s /bin/bash devuser

# Set the working directory
WORKDIR /app

# Ensure /app is owned by the new user
RUN chown -R devuser:devuser /app

# Switch to the non-root user for security and safety
USER devuser

# Ensure pip installed binaries are in the PATH
ENV PATH="/home/devuser/.local/bin:${PATH}"

# Rule D: Optional Dependency Management
# Using a wildcard (requirements.tx[t]) prevents the COPY command from failing if the file doesn't exist
COPY --chown=devuser:devuser requirements.tx[t] ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir --user -r requirements.txt; fi

# Rule B: Keep-Alive so the container stays awake in the background
CMD ["tail", "-f", "/dev/null"]
