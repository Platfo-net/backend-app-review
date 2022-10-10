"""attachment type and caption

Revision ID: aff60aa8e45d
Revises: d2b018c597f4
Create Date: 2022-09-10 15:21:24.716193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aff60aa8e45d'
down_revision = 'd2b018c597f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('content_attachments', sa.Column('attachment_type', sa.String(length=256), nullable=True))
    op.add_column('contents', sa.Column('caption', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contents', 'caption')
    op.drop_column('content_attachments', 'attachment_type')
    # ### end Alembic commands ###